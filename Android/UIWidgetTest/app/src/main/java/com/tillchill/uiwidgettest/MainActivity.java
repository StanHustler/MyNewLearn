package com.tillchill.uiwidgettest;

import androidx.appcompat.app.AlertDialog;
import androidx.appcompat.app.AppCompatActivity;

import android.app.ProgressDialog;
import android.content.DialogInterface;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.ProgressBar;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        Button button1 = (Button) findViewById(R.id.button);
        EditText editText1 = (EditText) findViewById(R.id.edit_text);
        ImageView imageView1 = (ImageView) findViewById(R.id.image_view);
        ProgressBar pb1 = (ProgressBar) findViewById(R.id.progress_bar);

        button1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                String inputText = editText1.getText().toString();
                Toast.makeText(MainActivity.this,inputText,Toast.LENGTH_SHORT).show();
//                imageView1.setImageResource(R.drawable.img_2);
/*                if(pb1.getVisibility() == View.GONE){
                    pb1.setVisibility(View.VISIBLE);
                }else {
                    pb1.setVisibility(View.GONE);
                }*/
                int progress = pb1.getProgress();
                progress += 10;
                pb1.setProgress(progress);

                ProgressDialog pd = new ProgressDialog(MainActivity.this);
                pd.setTitle("title");
                pd.setMessage("Loading");
                pd.setCancelable(true);
                pd.show();
            }
        });


    }
}