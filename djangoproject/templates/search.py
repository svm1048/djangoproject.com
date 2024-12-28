def search(context):
    request = context["request"]
    version = context["version"] if "version" in context else context["DJANGO_VERSION"]
    lang = context["lang"] if "lang" in context else context["LANGUAGE_CODE"]
    release = DocumentRelease.objects.get_by_version_and_lang(
        version,
        lang,
    )
    return {
        "form": DocSearchForm(request.GET, release=release),
        "version": version,
        "lang": lang,
    }