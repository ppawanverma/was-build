# -*- coding: utf-8 -*-

def main():

    #Goes through each node
    for node in AdminConfig.list('Node').split():
        #Acquire node name
        nodeName = AdminConfig.showAttribute(node, 'name')
        for server in AdminControl.queryNames("type=Server,node="+ nodeName + ",*").split():
            #Acquire server name
            serverName = AdminControl.getAttribute(server, 'name')
            print("serverName " + serverName)
            #Instrument JVM profiler
            AdminTask.setJVMProperties('[-nodeName ' + nodeName + ' -serverName ' + serverName + ' -genericJvmArguments "-agentlib:pmiJvmtiProfiler"]')
            AdminConfig.save()
            print("Finished instrumenting GC profiler")

if __name__ == "__main__":
    main()
setPMI.py

# -*- coding: utf-8 -*-

def main():

    #Enables all specified attributes
    customString = [append(), java.lang.Boolean ('true')]
    #Goes through each node
    for node in AdminConfig.list('Node').split():
        nName = AdminConfig.showAttribute(node, 'name')
        #Makes sure to not include the cell manager nodes
        for server in AdminControl.queryNames("type=Server,node="+ nName + ",*").split():
            #This obtains the Performance Mbean object.
            #First it gets the MBean name (i.e perfStr)
            #SEcond it obtains the Mbean Object (I.e perfObj)
            processName = AdminControl.getAttribute(server, 'name')
            perfStr = AdminControl.queryNames("type=Perf,process=" + processName + ",node=" + nName + ",*")
            perfObj = AdminControl.makeObjectName(perfStr)

            print("configuring:" + processName + ". From: " + nName)
            invoke(perfStr, perfObj, customString)
            print("done")

#Below is how you would ENABLE or DISABLE specific PMI stats/attributes.
#The attribute IDs/Numbers are derived from: https://www.ibm.com/support/knowledgecenter/en/SSAW57_9.0.5/com.ibm.websphere.nd.multiplatform.doc/ae/rprf_datacounter14.html
def append():
    string ='servletSessionsModule=6,1,2,7'
    string+=':beanModule=11,12'
    string+=':webAppModule=11,13'
    string+=':threadPoolModule=3,8,6,4,7'
    string+=':StatGroup.SIBService=8,14'
    string+=':StatGroup.SIBService>StatGroup.Communications>StatGroup.Clients>StatGroup.ClientsStandard=563,562'
    string+=':StatGroup.SIBService>StatGroup.Communications>StatGroup.MessagingEngines>StatGroup.MessagingEnginesStandard='
    string+=':StatGroup.SIBService>StatGroup.SIBMessagingEngines=513,512'
    string+=':systemModule=1,2,3'
    string+=':j2cModule=2,15,1,6,14,12,13,7'
    string+=':connectionPoolModule=2,15,1,6,14,12,13,7'
    string+=':jvmRuntimeModule=1,2,3,4,5,11,12,13'
    string+=':beanModule=11,12'
    return string

def invoke(perfStr, perfObj, customString):
    sigs = ['java.lang.String', 'java.lang.Boolean']
    AdminControl.invoke_jmx (perfObj, 'setCustomSetString', customString, sigs)
    AdminControl.invoke(perfStr,'savePMIConfiguration')

if __name__ == "__main__":
    main()