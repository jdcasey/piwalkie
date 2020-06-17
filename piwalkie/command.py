import click
import piwalkie.config as config
import piwalkie.convo as convo

@click.command()
@click.option('--config-file', '-c', help='Alternative config YAML')
def bot(config_file=None):
    cfg = config.load(config_file)
    convo.print_help()
    convo.start(cfg)
