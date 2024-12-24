import click
import frappe


def execute():

	click.secho(
		"LMS Module has been removed from the Education App. "
		"There is a new app for it called the AiBizzApp LMS. "
		"You can install the app from AiBizzHub Cloud Marketplace.\n"
		"https://aibizzhub.io/marketplace",
		fg="yellow",
	)
