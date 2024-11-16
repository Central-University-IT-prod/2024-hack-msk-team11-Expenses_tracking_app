
'use client'

import React, {useEffect, useState} from 'react';
import Router from 'next/router';
import Script from 'next/script';
import { usePathname, useRouter, useSearchParams, } from 'next/navigation';
import EventList from './components/EventList'


export default function index() {
  const [user_id, setUserId] = useState('');
  const [title, setTitle] = useState('');
  const [test_amount, setAmount] = useState(0)
  const [mainButtonClicked, setMainButtonClicked] = useState(false)
  const [error_message, setErrorMessage] = useState(null);


  const router = useRouter();

  const [loading, setLoading] = useState();

  const getUserId = async () => {
    if (window.Telegram.WebApp) {
      try{
        const tmp_user_id = await window.Telegram.WebApp.initDataUnsafe.user.id;

        if(tmp_user_id){
          setUserId(tmp_user_id);

          const response = await fetch('/pinguins', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
            },
            body: JSON.stringify({id: tmp_user_id})
          });

        }
      }
      catch(error){
        console.log(error);
      }
    }
  }

  useEffect(() => {
    getUserId();
  }, [])

  useEffect(() => {
    if(mainButtonClicked){
      if(title === ''){
        setErrorMessage('Введите название комнаты')
      }
      else{
        addEvent();
      }

    }
  }, [mainButtonClicked, title])

  const handleClickSendSum = () => {
    SendNum();
  }

  const addEvent = async () => {

    
    const url = '/events/';

    try{
      setLoading(true);
      const response = await fetch(url, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          title: title,
          owner: user_id,
        }),
      });

      if(response.ok){
        Router.push('/event')
        const data = await response.json();
        if(data){
          console.log(data)
        }
        else{
          console.error('Error: Нет даты');
          setErrorMessage(data.error);
        }
      }
    }
    catch (error){
      console.error(error);
      setErrorMessage(error.toString())
    } finally{
      setLoading(false);
    }
}

  useEffect(() => {
    const tg = window.Telegram.WebApp;
    tg.MainButton.show()
    tg.MainButton.setText('Создать комнату');
    tg.onEvent('mainButtonClicked',()=>{setMainButtonClicked(true);});

    tg.setHeaderColor('secondary_bg_color');
    tg.setBackgroundColor('secondary_bg_color');
    tg.expand();
    tg.BackButton.hide();

  }, []);


  return (
    <div className='wrapper'>
      <header className='header flex justify-center pt-10'>
        <Script src='static/telegram-web-app.js' strategy='beforeInteractive'></Script>
        <Script src="https://cdn.jsdelivr.net/npm/eruda" onLoad={() => {eruda.init()}}></Script>
        <div id='test' className='text-center '>
          <h1 className='m-5 text-4xl'>Мои комнаты</h1>
        </div>
      </header>
      <main className='main'>

        <div className='mt-10 flex justify-center flex-col'>
          <p className='self-center'>Введите название комнаты</p>
          <input  className=" self-center text-black m-5 p-0 w-1/3 border-0 text-center focus:ring-0 [&::-webkit-inner-spin-button]:appearance-none [&::-webkit-outer-spin-button]:appearance-none" style={{appearance: 'textfield'}}
            onChange={ (e) => {setTitle(e.target.value)} }
            value = {title}
          />
        </div>

        {error_message !== null ? (
          <div>
            <h1>{error_message}</h1>
          </div>
        ) : null
      }
      {user_id ? (
        <EventList
        user_id = {user_id}
      />
      ) : (
        <div className='flex justify-center'>
          <h1 className='text-3xl'>
            Комнат нет
          </h1>
        </div>
      )

      }



      </main>
    </div>
    
          
       
  )
}