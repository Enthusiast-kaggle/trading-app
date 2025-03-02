import 'package:flutter/material.dart';
import '../services/api.dart';

class TradeScreen extends StatefulWidget {
  @override
  _TradeScreenState createState() => _TradeScreenState();
}

class _TradeScreenState extends State<TradeScreen> {
  double prediction = 0.0;

  void getPrediction() async {
    List<double> features = [100.0, 101.5, 98.2, 100.5]; // Example OHLC values
    double result = await ApiService.predictStock(features);
    setState(() {
      prediction = result;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("Stock Prediction")),
      body: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Text("Predicted Price: \$${prediction.toStringAsFixed(2)}"),
          ElevatedButton(
            onPressed: getPrediction,
            child: Text("Predict"),
          ),
        ],
      ),
    );
  }
}
