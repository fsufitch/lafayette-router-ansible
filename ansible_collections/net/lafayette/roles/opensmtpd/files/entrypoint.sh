#!/bin/sh
set -e

SPOOL="/var/spool/smtpd"
SECRETS_SRC="/mnt/smtpd_secrets"
SECRETS_DST="/opt/smtpd_secrets"

mkdir -p "${SPOOL}"

mkdir -p "${SECRETS_DST}"
if [ -d "${SECRETS_SRC}" ]; then
  # Choose an existing smtpd group (_smtpd preferred, fallback to smtpd)
  SECRET_GROUP="_smtpd"
  getent group "${SECRET_GROUP}" >/dev/null 2>&1 || SECRET_GROUP="smtpd"

  cp -a "${SECRETS_SRC}/." "${SECRETS_DST}/"
  chown -R root:"${SECRET_GROUP}" "${SECRETS_DST}"
  find "${SECRETS_DST}" -type d -exec chmod 0750 {} +
  find "${SECRETS_DST}" -type f -exec chmod 0640 {} +
fi

exec /usr/sbin/smtpd -d -f /etc/smtpd/smtpd.conf
