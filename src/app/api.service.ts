import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class ApiService {
  private apiUrl = 'http://localhost:5000'; // Changez l'URL de l'API si nécessaire

  constructor(private http: HttpClient) {}

  getProducts(): Observable<any> {
    return this.http.get(`${this.apiUrl}/api/products`);
  }

  analyzeStrategy(payload: any): Observable<any> {
    return this.http.post(`${this.apiUrl}/api/analyze`, payload);
  }
}
