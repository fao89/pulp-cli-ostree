import click
from pulpcore.cli.common.context import PulpContext, pass_pulp_context
from pulpcore.cli.common.generic import (
    common_remote_create_options,
    common_remote_update_options,
    create_command,
    destroy_command,
    href_option,
    label_command,
    label_select_option,
    list_command,
    name_option,
    show_command,
    update_command,
)

from pulpcore.cli.ostree.context import PulpOstreeRemoteContext


@click.group()
@click.option(
    "-t",
    "--type",
    "remote_type",
    type=click.Choice(["ostree"], case_sensitive=False),
    default="ostree",
)
@pass_pulp_context
@click.pass_context
def remote(ctx: click.Context, pulp_ctx: PulpContext, remote_type: str) -> None:
    if remote_type == "ostree":
        ctx.obj = PulpOstreeRemoteContext(pulp_ctx)
    else:
        raise NotImplementedError()


lookup_options = [href_option, name_option]
ostree_remote_options = [
    click.option("--policy", type=click.Choice(["immediate", "on_demand"], case_sensitive=False)),
    click.option("--depth", type=click.INT, default=0),
]

remote.add_command(list_command(decorators=[label_select_option]))
remote.add_command(show_command(decorators=lookup_options))
remote.add_command(create_command(decorators=common_remote_create_options + ostree_remote_options))
remote.add_command(
    update_command(decorators=lookup_options + common_remote_update_options + ostree_remote_options)
)
remote.add_command(destroy_command(decorators=lookup_options))
remote.add_command(label_command())
