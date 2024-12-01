import { Component } from '@angular/core';
import { ApiService } from '../api.service';
import {FormsModule} from '@angular/forms';

@Component({
  selector: 'app-analyze-form',
  standalone: true,
  imports: [
    FormsModule
  ],
  templateUrl: './analyze-form.component.html',
  styleUrls: ['./analyze-form.component.scss'],
})
export class AnalyzeFormComponent {
  strategy = '';
  symbol = '';
  start_date = '';
  end_date = '';

  constructor(private apiService: ApiService) {}

  onSubmit() {
    const payload = {
      strategy: this.strategy,
      product_symbol: this.symbol,
      start_date: this.start_date,
      end_date: this.end_date,
    };
    this.apiService.analyzeStrategy(payload).subscribe((result) => {
      console.log(result);
    });
  }
}
