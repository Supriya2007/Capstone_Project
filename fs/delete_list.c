 void delete(list* lint key)
 {  
     node* pres=l->head;
     node* prev=NULL;
     while(pres && pres->key!=key)
     {
         prev=pres;
         pres=pres->link;
     }

     if(prev && pres)
     {
         prev->link=pres->link;
     }
     else
     {
         l->head=pres->link;
     }
     

 }