def compact_list(values):
    return [str(value).strip() for value in values if value is not None and str(value).strip()]
