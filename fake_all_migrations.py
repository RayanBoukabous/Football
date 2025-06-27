from django.core.management import call_command
from django.apps import apps


def mark_all_migrations_as_fake():
    for app_config in apps.get_app_configs():
        app_label = app_config.label
        print(f"Marking all migrations for app '{app_label}' as applied")
        call_command("migrate", app_label, fake=True)


if __name__ == "__main__":
    mark_all_migrations_as_fake()
