import json

def save_report(report, json_path, text_path):
    with open(json_path, "w") as f:
        json.dump(report, f, indent=4)

    with open(text_path, "w") as f:
        f.write("SUMMARY:\n" + report['summary'] + "\n\n")
        f.write("INSIGHTS:\n" + report['insights'] + "\n\n")
        f.write("ACTIONS:\n" + report['actions'])
