from routing import splitRoute,initPorts,link_item,delPorts,delExtraRoute
from libs import Get_full_route_by_XY,Get_link_index_by_route,Update_link_set,getMaxOne

#spiltRoute(0,0,8,[],3,80)
#print(Get_full_route_by_XY([],0,5,4))
#print(getMaxOne([1,2,33,5,4]))
src=13
des=14
print(initPorts(src,4,des,mode=0))
print(initPorts(des,4,src,mode=1))
"""
num_of_rows=4
link_set=[]
total_link_num=(num_of_rows-1+num_of_rows)*(num_of_rows-1)+num_of_rows-1
for i in range(0,total_link_num):
    tmp=link_item()
    link_set.append(tmp)
Update_link_set([[1, 'E']],link_set,num_of_rows,0,1)
contention,route=splitRoute(5,10,num_of_rows,link_set,4,0,10)
print(contention,route)
"""
