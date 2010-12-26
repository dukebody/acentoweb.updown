#!/bin/sh
i18ndude rebuild-pot --pot locales/acentoweb.updown.pot --create acentoweb.updown .
i18ndude sync --pot locales/acentoweb.updown.pot locales/*/LC_MESSAGES/acentoweb.updown.po
