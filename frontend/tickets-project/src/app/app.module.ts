import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { WrapperComponent } from './wrapper/wrapper.component';
import { NoopAnimationsModule } from '@angular/platform-browser/animations';
import {MatListModule} from '@angular/material/list';
import {MatDividerModule} from '@angular/material/divider';
import {MatExpansionModule} from '@angular/material/expansion';
import {MatIconModule} from '@angular/material/icon';
import {MatRippleModule} from '@angular/material/core';
import { TicketComponent } from './ticket/ticket.component';

@NgModule({
  declarations: [
    AppComponent,
    WrapperComponent,
    TicketComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    AppRoutingModule,
    NoopAnimationsModule,
    MatListModule,
    MatDividerModule,
    MatExpansionModule,
    MatIconModule,
    MatRippleModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
