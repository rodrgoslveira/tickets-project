import { Component, OnInit } from '@angular/core';
import { Ticket } from '../ticket-interface';
import {TicketApiService} from '../ticket-api.service'

@Component({
  selector: 'app-wrapper',
  templateUrl: './wrapper.component.html',
  styleUrls: ['./wrapper.component.scss']
})
export class WrapperComponent implements OnInit {
  currentTickets:Ticket[] 
  constructor( private ticketsService: TicketApiService) { }

  ngOnInit(): void {
    this.ticketsService.getTickets()
        .subscribe( resp => {
          this.currentTickets = resp;
        });
  }

}
