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