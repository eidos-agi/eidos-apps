# Declaration fixture. Not Eidos Video.
# Declared, not running. Capture stays in video-3d-forge.
FROM alpine:3.20
WORKDIR /app
COPY app.json /app/app.json
VOLUME /packs
EXPOSE 8080
LABEL eidos.app=eidos-video
CMD ["cat", "/app/app.json"]
