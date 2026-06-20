package com.myvpn.app

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.unit.dp

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            MaterialTheme(colorScheme = darkColorScheme()) {
                VPNMainScreen()
            }
        }
    }
}

@Composable
fun VPNMainScreen() {
    var isConnected by remember { mutableStateOf(false) }

    Column(
        modifier = Modifier.fillMaxSize().background(Color(0xFF0B0E14)),
        horizontalAlignment = Alignment.CenterHorizontally,
        verticalArrangement = Arrangement.Center
    ) {
        Text(if (isConnected) "ЗАЩИЩЕНО" else "ОТКЛЮЧЕНО", color = Color.White)
        
        Spacer(modifier = Modifier.height(50.dp))
        
        // Кнопка подключения
        Button(
            onClick = { isConnected = !isConnected },
            modifier = Modifier.size(150.dp),
            shape = CircleShape,
            colors = ButtonDefaults.buttonColors(
                containerColor = if (isConnected) Color(0xFF00C853) else Color(0xFFD50000)
            )
        ) {
            Text("CONNECT")
        }
    }
}
