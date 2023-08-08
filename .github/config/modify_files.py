import os
import sys
import yaml


def modify_chart_yaml(directory, new_version):
    chart_file_path = os.path.join(directory, "Chart.yaml")

    if os.path.exists(chart_file_path):
        with open(chart_file_path, "r") as chart_file:
            chart_data = yaml.safe_load(chart_file)

        chart_data["version"] = new_version

        with open(chart_file_path, "w") as chart_file:
            yaml.dump(chart_data, chart_file, default_flow_style=False)

        print(f"Modified Chart.yaml in '{directory}' to version {new_version}")
    else:
        print(f"Chart.yaml not found in '{directory}'")


def main():
    if len(sys.argv) != 3:
        print("Usage: python modify_chart_versions.py <folder_path> <new_version>")
        sys.exit(1)

    folder_path = sys.argv[1]
    new_version = sys.argv[2]

    if not os.path.isdir(folder_path):
        print("Error: The specified path is not a directory.")
        sys.exit(1)

    for directory in os.listdir(folder_path):
        full_dir_path = os.path.join(folder_path, directory)
        if os.path.isdir(full_dir_path):
            modify_chart_yaml(full_dir_path, new_version)


if __name__ == "__main__":
    main()
