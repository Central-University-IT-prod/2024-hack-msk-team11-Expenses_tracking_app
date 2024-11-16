
'use client'

import React, {useEffect, useState} from 'react';
import Router from 'next/router';
import Script from 'next/script';
import { usePathname, useRouter, useSearchParams, } from 'next/navigation';


export default function EventList(props) {
  const user_id = props.user_id;
  const [data, setData] = useState([])

  const eventList = async () => {
    
    const url = `/pinguins/${user_id}/events` ;

    try{
      const response = await fetch(url, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
        },
      });

      if(response.ok){

        const res = await response.json();
        if(res){
          console.log(res)
          setData(res)
        }
        else{
          console.error('Error: Нет даты');
        }
      }
    }
    catch (error){
      console.error(error);
    }
}

useEffect(() => {
  void eventList();
}, [])


  return (
    <div>
        <ul>
            {data.map(data => (
                <li>
                    <div className='flex flex-col text-black'>
                        <p>id - {data.id}</p>
                        <p>created_at - {data.created_at}</p>
                        <p>title - {data.title}</p>
                        <p>link - {data.link}</p>
                        <p>owner - {data.owner}</p>
                    </div>
                </li>
                
            ))}

        </ul>
    </div>
    
          
       
  )
}