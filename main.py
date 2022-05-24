import sys
import panflute

headers = dict()


def pandoc_filter(element, doc):
    if isinstance(element, panflute.Str) and element.text.lower() == "bold":
        return panflute.Strong(element)

    if isinstance(element, panflute.Header) and element.level <= 3:
        return element.walk(str_up)

    if isinstance(element, panflute.Header):
        text = panflute.stringify(element)
        if text in headers.keys():
            if not headers[text]:
                sys.stderr.write(f"Header repeated: \"{text}\"")
                headers[text] = True
        else:
            headers[text] = False


def str_up(element, doc):
    if isinstance(element, panflute.Str):
        element.text = element.text.upper()


def main(doc=None):
    return panflute.run_filter(pandoc_filter, doc=doc)


if __name__ == "__main__":
    main()
