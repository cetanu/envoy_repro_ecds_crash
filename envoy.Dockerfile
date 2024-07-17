FROM envoyproxy/envoy:v1.28.3
ADD envoy.yaml /srv/envoy.yaml
CMD envoy --log-level ${ENVOY_LOGLEVEL} -c /srv/envoy.yaml
