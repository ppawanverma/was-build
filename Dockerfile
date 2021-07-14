#FROM ibmcom/websphere-traditional:latest as base
FROM ppawanverma/demo:metrics-9.0.5.8
#FROM ibmcom/websphere-traditional:latest
#COPY --from=base --chown=was:root /opt/IBM/WebSphere/AppServer/installableApps/metrics.ear /work/config/metrics.ear
COPY --chown=was:root installApp.py /work/config/
COPY --chown=was:root setPMI.py setGCProfiler.py /work/
COPY was-config.props /work/config/was-config.props
RUN env JVM_EXTRA_CMD_ARGS=-Xnoloa /work/configure.sh && /work/configure.sh /work/setGCProfiler.py && /work/configure.sh /work/setPMI.py