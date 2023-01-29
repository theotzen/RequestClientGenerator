from utils import *
import sys

base_imports_async = "\"\"\"\n@theotzenRequestBundleGenerator\n" \
                     "This file is autogenerated from FastAPI routers\n\"\"\"\n\n" \
                     "import httpx\nimport os\nfrom dotenv import load_dotenv\nfrom fastapi import HTTPException\n" \
                     "from fastapi.encoders import jsonable_encoder\nfrom app.core.log_config import init_loggers\n\n" \
                     "loggerIH = init_loggers(__name__)\n\nload_dotenv()\n\n" \
                     "base_url = os.getenv(__name__)\n\nclient = httpx.AsyncClient()"

base_imports_sync = "\"\"\"\n@theotzenRequestBundleGenerator\n" \
                    "This file is autogenerated from FastAPI routers\n\"\"\"\n\n" \
                    "import httpx\nimport os\nfrom dotenv import load_dotenv\nfrom fastapi import " \
                    "HTTPException\n" \
                    "from fastapi.encoders import jsonable_encoder\nfrom app.core.log_config import " \
                    "init_loggers\n\n" \
                    "loggerIH = init_loggers(__name__)\n\nload_dotenv()\n\nbase_url = os.getenv(" \
                    "__name__)"


def write_functions_to_python_file_with_path(path_to_write_in: str,
                                             func_dict: dict,
                                             base_imports: str):
    for key in func_dict.keys():
        final_path = path_to_write_in + "/" + key + "_req.py"
        to_write = "\n\n\n".join(func_dict[key])
        with open(final_path, 'w') as f:
            f.write(base_imports + "\n\n\n")
            f.write(to_write)
            f.close


def from_json_to_writing(base_url: str,
                         path_to_write_in: str,
                         async_client: bool):
    json_url = base_url + '/openapi.json'
    all_json = from_json_to_functions(json_url=json_url, async_client=async_client)
    if async_client:
        base_imports = base_imports_async
    else:
        base_imports = base_imports_sync
    write_functions_to_python_file_with_path(path_to_write_in=path_to_write_in, func_dict=all_json,
                                             base_imports=base_imports)


if __name__ == '__main__':
    # Map command line arguments to function arguments.
    from_json_to_writing(*sys.argv[1:])
