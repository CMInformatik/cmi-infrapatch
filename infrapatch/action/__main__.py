import logging as log


import click
from github import Auth, Github, GithubException
from github.PullRequest import PullRequest
from infrapatch.action.config import ActionConfigProvider

from infrapatch.core.provider_handler_builder import ProviderHandlerBuilder
from infrapatch.core.log_helper import catch_exception, setup_logging
from infrapatch.core.utils.git import Git


@click.group(invoke_without_command=True)
@click.option("--debug", is_flag=True)
@catch_exception(handle=Exception)
def main(debug: bool):
    setup_logging(debug)

    config = ActionConfigProvider()

    git = Git(config.repository_root)
    github = Github(auth=Auth.Token(config.github_token))
    github_repo = github.get_repo(config.repository_name)
    github_head_branch = github_repo.get_branch(config.head_branch)

    if len(config.enabled_providers) == 0:
        raise Exception("No providers enabled. Please enable at least one provider.")

    builder = ProviderHandlerBuilder(config.working_directory)
    builder.with_git_integration()
    if "terraform_modules" in config.enabled_providers or "terraform_providers" in config.enabled_providers:
        builder.add_terraform_registry_configuration(config.default_registry_domain, config.registry_secrets)
    if "terraform_modules" in config.enabled_providers:
        builder.with_terraform_module_provider()
    if "terraform_providers" in config.enabled_providers:
        builder.with_terraform_provider_provider()

    provider_handler = builder.build()

    git.fetch_origin()

    try:
        github_target_branch = github_repo.get_branch(config.target_branch)
    except GithubException:
        github_target_branch = None

    if github_target_branch is not None and config.report_only is False:
        log.info(f"Branch {config.target_branch} already exists. Checking out...")
        git.checkout_branch(config.target_branch, f"origin/{config.target_branch}")

        log.info(f"Rebasing branch {config.target_branch} onto origin/{config.head_branch}")
        git.run_git_command(["rebase", "-Xtheirs", f"origin/{config.head_branch}"])
        git.push(["-f", "-u", "origin", config.target_branch])

    if config.report_only:
        provider_handler.print_resource_table(only_upgradable=True)
        log.info("Report only mode is enabled. No changes will be applied.")
        return

    if provider_handler.check_if_upgrades_available() is False:
        log.info("No resources with pending upgrade found.")
        return

    if github_target_branch is None:
        log.info(f"Branch {config.target_branch} does not exist. Creating and checking out...")
        github_repo.create_git_ref(ref=f"refs/heads/{config.target_branch}", sha=github_head_branch.commit.sha)
        git.checkout_branch(config.target_branch, f"origin/{config.head_branch}")

    provider_handler.upgrade_resources()
    provider_handler.print_statistics_table()
    provider_handler.dump_statistics()

    git.push(["-f", "-u", "origin", config.target_branch])

    create_pr(config.github_token, config.head_branch, config.repository_name, config.target_branch)


def create_pr(github_token, head_branch, repository_name, target_branch) -> PullRequest:
    token = Auth.Token(github_token)
    github = Github(auth=token)
    repo = github.get_repo(repository_name)
    pull = repo.get_pulls(state="open", sort="created", base=head_branch, head=target_branch)
    if pull.totalCount != 0:
        log.info(f"Pull request found from '{target_branch}' to '{head_branch}'")
        return pull[0]
    log.info(f"No pull request found from '{target_branch}' to '{head_branch}'. Creating a new one.")
    return repo.create_pull(title="InfraPatch Module and Provider Update", body="InfraPatch Module and Provider Update", base=head_branch, head=target_branch)


if __name__ == "__main__":
    main()
