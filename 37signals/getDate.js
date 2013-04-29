<script language="javascript">
var DayOfWeek;
function fncDayOfWeek() 
{ 
var stDate; 
var now; 
var assoc= new Array(7); 
assoc[0]="Sunday"; 
assoc[1]="Monday"; 
assoc[2]="Tuesday"; 
assoc[3]="Wednesday"; 
assoc[4]="Thursday"; 
assoc[5]="Friday"; 
assoc[6]="Saturday"; 
now= new Date(); 
stDate=now.getDay(); 

}
document.write('<B>Current Day of the Week:</b>' + (assoc[stDate])); 
</script>