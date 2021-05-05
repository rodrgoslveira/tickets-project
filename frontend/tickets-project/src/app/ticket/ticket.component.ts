import { Component, OnInit, Input } from '@angular/core';
import { Ticket } from '../ticket-interface';

@Component({
  selector: 'app-ticket',
  templateUrl: './ticket.component.html',
  styleUrls: ['./ticket.component.scss']
})
export class TicketComponent implements OnInit {

  @Input() current_ticket: Ticket;

  constructor() { }

  ngOnInit(): void {
  }

}
