javaagent https://github.com/prometheus/jmx_exporter
����javaagent��https://repo1.maven.org/maven2/io/prometheus/jmx/jmx_prometheus_javaagent/0.3.1/jmx_prometheus_javaagent-0.3.1.jar

kubernetes���jvm
ÿ��Ӧ�ö�ͨ��javaagent�����ṩһ��http����¶���Լ���JMX��Ϣ��prometheusͨ��kubernetes �Զ����־��ܰ����Ӧ�ü����ض����б����������ռ������ٷ����״̬��
``` 
 annotations:
        prometheus.io/scrape: "true"
        prometheus.io/port: "8090"
        prometheus.io/path: /metrics
```		
spec.template.metadata.annotations.prometheus.io/scrape
�Ƿ����Discorvery
spec.template.metadata.annotations.prometheus.io/port
����Ŀ��˿�
spec.template.metadata.annotations.prometheus.io/path
����Ŀ��·��

����һ��configmap
``` 
kubectl create cm prometheus-jmx-exporter-config --from-file=./config.yaml
kubectl apply -f tomcat-monitoring-demo.yaml
[root@centos-master jvm-exporter]# kubectl  get pod | grep demo 
tomcat-monitoring-demo-1780394632-c96hz              1/1       Running            0          1h
tomcat-monitoring-demo-1780394632-sk09b              1/1       Running            0          1h
```
��javaagent��nfs�������û��nfs���Կ�����ӵ������������dockerfileʱ�����
grafana ����Ǳ���id:7727


prometheus�����ļ����
```
    - job_name: 'kubernetes-pods'
      kubernetes_sd_configs:
      - role: pod
      relabel_configs:
      - source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_scrape]
        action: keep
        regex: true
      - source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_path]
        action: replace
        target_label: __metrics_path__
        regex: (.+)
      - source_labels: [__address__, __meta_kubernetes_pod_annotation_prometheus_io_port]
        action: replace
        regex: ([^:]+)(?::\d+)?;(\d+)
        replacement: $1:$2
        target_label: __address__
      - action: labelmap
        regex: __meta_kubernetes_pod_label_(.+)
      - source_labels: [__meta_kubernetes_namespace]
        action: replace
        target_label: kubernetes_namespace
      - source_labels: [__meta_kubernetes_pod_name]
        action: replace
        target_label: kubernetes_pod_name
```
ʹ��docker����
 docker run -d   --name tomcat-jmx   -v ~/jvm-exporter:/jmx-exporter   -e CATALINA_OPTS="-Xms1G -Xmx1G -javaagent:/jmx-exporter/jmx_prometheus_javaagent-0.3.1.jar=6060:/jmx-exporter/config.yml"   -p 6060:6060   -p 9090:8080   tomcat:latest
