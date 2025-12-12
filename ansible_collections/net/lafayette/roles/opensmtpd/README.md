# `opensmtpd`

Containerized OpenSMTPD submission service that listens on the LAN and relays outbound mail to Amazon SES. Intended for printer "scan-to-email" support where the printer uses short credentials locally and the relay holds SES SMTP credentials.

## Role configuration

| Variable | Default | Purpose |
| --- | --- | --- |
| opensmtpd_dir | /opt/lafayette/opensmtpd | Base directory for config/secrets/spool |
| opensmtpd_image_build | true | Build the bundled Alpine-based image |
| opensmtpd_image | lafayette-opensmtpd | Image tag |
| opensmtpd_container_name | lafayette-opensmtpd | Quadlet unit name |
| opensmtpd_listen_addrs | [] | Addresses to bind for submission (required) |
| opensmtpd_submission_port | 587 | Submission port |
| opensmtpd_require_starttls | true | Require STARTTLS on submission |
| opensmtpd_pki_name | lafayette-opensmtpd | PKI label for TLS |
| opensmtpd_pki_cert / opensmtpd_pki_key | "" | Paths to cert/key on host (required when STARTTLS is enforced) |
| opensmtpd_manage_secrets | true | If true, render SES/printer secret tables from vars; if false, expect files to exist on host |
| opensmtpd_printer_auth_enabled | false | Require SMTP AUTH for printer submissions |
| opensmtpd_printer_username / opensmtpd_printer_password | "" | Credentials the printer uses for SMTP AUTH |
| opensmtpd_allowed_srcs | [] | Source CIDRs allowed to relay without auth |
| opensmtpd_ses_region | us-east-1 | SES region used for SMTP endpoint |
| opensmtpd_ses_smtp_host | email-smtp.{{ opensmtpd_ses_region }}.amazonaws.com | SES SMTP host |
| opensmtpd_ses_smtp_port | 587 | SES SMTP port |
| opensmtpd_ses_smtp_username / opensmtpd_ses_smtp_password | "" | SES SMTP credentials (required) |
| opensmtpd_envelope_mail_from | "" | Optional forced envelope sender for SES |

Generated files:

- `{{ opensmtpd_config_dir }}/smtpd.conf` &mdash; OpenSMTPD configuration
- `{{ opensmtpd_secrets_dir }}/ses_secrets` &mdash; SES SMTP credentials table
- `{{ opensmtpd_secrets_dir }}/printer_secrets` &mdash; printer AUTH credentials table (when provided)
- `podman-{{ opensmtpd_container_name }}.service` &mdash; systemd quadlet unit

When `opensmtpd_manage_secrets` is false, the role will skip rendering `ses_secrets` and `printer_secrets`; create them manually on the host using the same paths and OpenSMTPD “label username:password” format.
