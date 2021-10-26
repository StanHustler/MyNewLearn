package com.tillchill.activitylifecycletest;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.util.Log;

public class NomalActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.nomal_layout);

        Intent intent=getIntent();
        Bundle bundle=intent.getBundleExtra("123");
        Log.d("Hello",bundle.getString("data_key"));

    }


}