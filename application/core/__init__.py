from .routes import ApplicationBlueprints

# Variables under this description is the blueprints which in future
# TODO: autofill for blueprints. Means autoupdate this file and autoimport them to \
# TODO: the __init__.py file (registering blueprints) into $ROOT/application folder
abp_instance = ApplicationBlueprints()


def get_blueprints_list():
    """

    This function contains list of existing blueprint applications. Fills manually right after adding a new
    blueprint into 'routes.py' file

    :return: list of the existing blueprints
    # TODO: we have template for naming (bpv_*) left only func autofill

    """
    blueprints_list = []

    bpv_projects = abp_instance.projects()
    blueprints_list.append(bpv_projects)
    bpv_index = abp_instance.index()
    blueprints_list.append(bpv_index)
    return blueprints_list
