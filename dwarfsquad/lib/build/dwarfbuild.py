from dwarfsquad.lib.build.from_zip import build_batch_from_zip
from dwarfsquad.lib.build.from_json import build_assay_configuration as build_ac_from_json
from dwarfsquad.lib.build.from_export import build_full_assay_configuration as build_ac_from_export
from dwarfsquad.lib.build.from_xlsx import build_full_ac as build_ac_from_xlsx
import dwarfsquad.lib.utils as utils


def dwarfbuild(data):

    if len(data) > 1:
        return process_list_of_data(data)
    elif len(data) == 1:
        data = data[0]
    else:
        raise Exception

    if utils.is_exported_assay(data):
        utils.to_stderr("Found exported assay at " + str(data))
        utils.to_stderr("Building assay configuration...")
        return build_ac_from_export(data)

    if utils.is_json_assay(data):
        utils.to_stderr("Found json assay at " + str(data))
        utils.to_stderr("Building assay configuration...")
        return build_ac_from_json(data)

    if utils.is_xlsx_file(data):
        utils.to_stderr("Found xlsx assay at " + str(data))
        utils.to_stderr("Building assay configuration...")
        return build_ac_from_xlsx(data)

    if utils.is_batch(data):
        utils.to_stderr("Found batch at " + str(data))
        utils.to_stderr("Posting batch to quartermaster...")
        return build_batch_from_zip(data)

    if utils.is_valid_oid(data) or isinstance(data, str):
        utils.to_stderr("Found string data at " + str(data))
        utils.to_stderr("Treating data like string query...")
        return data

    utils.to_stderr("Could not find any data at " + data + ". What is it you are trying to do?")
    return data


def process_list_of_data(data):
    pass
