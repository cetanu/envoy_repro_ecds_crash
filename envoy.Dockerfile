FROM envoyproxy/envoy:v1.28.3
ADD envoy.yaml /srv/envoy.yaml
CMD envoy -c /srv/envoy.yaml
