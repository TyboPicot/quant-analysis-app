import { Component } from '@angular/core';
import { ApiService } from '../api.service';

@Component({
  selector: 'app-product-list',
  standalone: true,
  imports: [],
  templateUrl: './product-list.component.html',
  styleUrls: ['./product-list.component.scss'],
})
export class ProductListComponent {
  products: any[] = [];

  constructor(private apiService: ApiService) {
    this.getProducts();
  }

  getProducts() {
    this.apiService.getProducts().subscribe((data) => {
      this.products = data;
    });
  }
}
