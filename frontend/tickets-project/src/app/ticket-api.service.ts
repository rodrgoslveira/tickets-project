import { Injectable } from '@angular/core';
import { HttpClient } from "@angular/common/http";
import { Ticket } from './ticket-interface';

@Injectable({
  providedIn: 'root'
})
export class TicketApiService {
  private apiUrl = "http://localhost:5000/"; // URL to web api

  constructor(private http: HttpClient) { }

  getTickets(){
    return this.http.get<Ticket[]>(this.apiUrl + 'getTickets')
  }
}
