def tabbyapi(branch, requires=None, default=False):
    pkg = package.copy()

    pkg["name"] = f"tabbyapi:{branch}"

    if requires:
        pkg["requires"] = requires

    if default:
        pkg["alias"] = "tabbyapi"

    pkg["build_args"] = {
        "TABBYAPI_BRANCH": branch,
    }

    return pkg


package = [
    tabbyapi("main", requires=">=36", default=True),
]
