from dwarfsquad.model.AssayConfiguration import AssayConfiguration
from dwarfsquad.lib.export.export_full_ac import export_full_ac
from dwarfsquad.lib import collections
from dwarfsquad.lib.export.export_compounds import export_compounds
from dwarfsquad.lib.export.export_lots_and_levels import export_lots_and_levels
from dwarfsquad.lib.export.export_assay_configuration import export_assay_configuration
from dwarfsquad.lib.export.export_rulesettings import export_rulesettings


def dwarfexport(url, data, collection, credentials):

    ac = None
    if isinstance(data, AssayConfiguration):
        ac = data

    if collection in collections.full_assay_configuration:
        export_full_ac(ac)

    elif collection in collections.assay_configuration:
        export_assay_configuration(ac)

    elif collection in collections.rule_settings:
        export_rulesettings(ac)

    elif collection in collections.compound_methods:
        export_compounds(ac)

    elif collection in collections.lots_and_levels:
        export_lots_and_levels(ac)

    elif data and collection in collections.rule_settings:
        export_rulesettings(ac)
