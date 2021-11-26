FROM fluent/fluentd:v1.14.2-debian-1.0

USER root
RUN mkdir -p /var/log/fluent/
RUN chown -R fluent /var/log/fluent/
# RUN ["gem", "install", "fluent-plugin-elasticsearch", "--no-document", "--version", "5.0.3"]
USER fluent
