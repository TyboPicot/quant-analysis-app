import { Routes } from '@angular/router';
import { ProductListComponent } from './product-list/product-list.component';
import { AnalyzeFormComponent } from './analyze-form/analyze-form.component';

export const routes: Routes = [
  { path: 'products', component: ProductListComponent },
  { path: 'analyze', component: AnalyzeFormComponent },
  { path: '', redirectTo: '/products', pathMatch: 'full' },
];
