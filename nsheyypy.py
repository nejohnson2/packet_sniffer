import subprocess

# def hop(channels, channelHopInterval): 
#   if (channelHopper) {
#     channelHopper.kill();
#   }

#   if (channelIndex < (channels.length-1) ){
#     channelIndex ++;
#   } else{
#     channelIndex = 0;
#   }

#   currentChannel = channels[channelIndex];

#   channelHopper = spawn('/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport', ['sniff', currentChannel]);

#   channelHopper.stdout.on('data', function (data) {
#     console.log('airport stdout: ' + data);
#   });

#   channelHopper.stderr.on('data', function (data) {
#     if(data){
#       tinsSniffer.kill();
#     }
#     console.log('airport stderr: ' + data);
#   });

#   if(channelHopInterval){
#     hopTimer = setTimeout(function(){
#       hop(channels, channelHopInterval);
#       }, channelHopInterval);
#   }
#   else{
#     hopTimer = setTimeout(function(channels){hop(channels);}, 5000, channels);
#   }

# def clearProcesses(cb):
#   var killall =spawn('killall', ['tinsSniffer']);

#   killall.on('exit',function(){
#     var killagain = spawn('killall', ['airport']);
#     killagain.on('exit',function(){
#       if(typeof cb === "function"){
#         cb();
#       }
#     });
#   });



def sniff():
	tinssniffer = subprocess.call(["./tinsSniffer"])

if __name__ == '__main__':
	sniff()