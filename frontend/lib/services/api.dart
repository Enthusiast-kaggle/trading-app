import 'dart:convert';
import 'package:http/http.dart' as http;

class ApiService {
  static const String baseUrl = "http://127.0.0.1:5000"; // Flask server URL

  static Future<double> predictStock(List<double> features) async {
    final response = await http.post(
      Uri.parse("$baseUrl/predict"),
      headers: {"Content-Type": "application/json"},
      body: jsonEncode({"features": features}),
    );
    if (response.statusCode == 200) {
      return jsonDecode(response.body)["prediction"];
    } else {
      throw Exception("Failed to fetch prediction");
    }
  }
}
