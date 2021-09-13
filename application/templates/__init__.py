from .url_factory import (get_file_names,
                          get_file_paths,
                          fill_url_dict
                          )

url_dict = fill_url_dict(get_file_names(), get_file_paths())
