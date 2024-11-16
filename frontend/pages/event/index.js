
import Script from 'next/script';
import { Root } from 'postcss';
import React, {useEffect, useState} from 'react';


export default function index() {



  useEffect(() => {
    const tg = window.Telegram.WebApp;

    tg.MainButton.hide();
    tg.BackButton.show();
    tg.setHeaderColor('secondary_bg_color');
    tg.setBackgroundColor('secondary_bg_color');

    tg.onEvent('backButtonClicked', () => {
      tg.BackButton.hide();
      tg.MainButton.hide();
      Router.back();
    });

    return () => {
      tg.offEvent('backButtonClicked');
    };
  }, []);


  return (
    <div className='wrapper'>
      <header className='header flex justify-center pt-10'>
        <Script src='static/telegram-web-app.js' strategy='beforeInteractive'></Script>
        <div id='test' className='text-center '>
          <h1 className='m-5 text-4xl'>Event page</h1>
        </div>
      </header>
      <main className='main'>
        <div className='mt-10 text-xl justify-center flex'>
          <p>test button</p>
        </div>
      </main>
    </div>
  )
}