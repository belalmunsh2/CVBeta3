<template>
  <div class="select-date-box">
    <div class="select-container">
      <select 
        v-model="selectedMonth" 
        class="select-dropdown"
        @change="emitDateChange"
      >
        <option value="" disabled selected>Month</option>
        <option v-for="(month, index) in months" :key="index" :value="month.value">
          {{ month.label }}
        </option>
      </select>
    </div>

    <div class="select-container">
      <select 
        v-model="selectedYear" 
        class="select-dropdown"
        @change="emitDateChange"
      >
        <option value="" disabled selected>Year</option>
        <option v-for="year in years" :key="year" :value="year">
          {{ year }}
        </option>
      </select>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, watch } from 'vue';

const props = defineProps({
  initialDate: {
    type: String,
    default: '',
  },
  yearStart: {
    type: Number,
    default: null,
  },
  yearEnd: {
    type: Number,
    default: null,
  },
  label: {
    type: String,
    default: '',
  }
});

const emit = defineEmits(['date-selected']);

const selectedMonth = ref('');
const selectedYear = ref('');

// Month names and their values
const months = [
  { value: '01', label: 'January' },
  { value: '02', label: 'February' },
  { value: '03', label: 'March' },
  { value: '04', label: 'April' },
  { value: '05', label: 'May' },
  { value: '06', label: 'June' },
  { value: '07', label: 'July' },
  { value: '08', label: 'August' },
  { value: '09', label: 'September' },
  { value: '10', label: 'October' },
  { value: '11', label: 'November' },
  { value: '12', label: 'December' }
];

// Generate a range of years (50 years back from current year to 5 years in the future)
const years = computed(() => {
  const currentYear = new Date().getFullYear();
  const start = props.yearStart ?? (currentYear - 50);
  const end = props.yearEnd ?? (currentYear + 5);
  
  const yearArray = [];
  for (let year = end; year >= start; year--) {
    yearArray.push(year.toString());
  }
  return yearArray;
});

// Emit event when both month and year are selected
const emitDateChange = () => {
  if (selectedMonth.value && selectedYear.value) {
    const formattedDate = `${selectedYear.value}-${selectedMonth.value}`;
    emit('date-selected', formattedDate);
  }
};

// Initialize from initialDate prop if provided
onMounted(() => {
  if (props.initialDate) {
    const [year, month] = props.initialDate.split('-');
    selectedYear.value = year;
    selectedMonth.value = month;
  }
});

// Watch for changes to initialDate prop
watch(() => props.initialDate, (newValue) => {
  if (newValue) {
    const [year, month] = newValue.split('-');
    selectedYear.value = year;
    selectedMonth.value = month;
  } else {
    selectedYear.value = '';
    selectedMonth.value = '';
  }
});
</script>

<style scoped>
.select-date-box {
  display: flex;
  gap: 0.75rem;
  width: 100%;
  margin-bottom: 1rem;
}

.select-container {
  position: relative;
  flex: 1;
}

.select-dropdown {
  width: 100%;
  padding: 0.625rem 0.75rem;
  border: 1px solid #e2e8f0;
  border-radius: 0.375rem;
  background-color: white;
  font-size: 0.875rem;
  line-height: 1.25rem;
  color: #1a202c;
  appearance: none;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 20 20' fill='%233498DB'%3E%3Cpath fill-rule='evenodd' d='M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z' clip-rule='evenodd' /%3E%3C/svg%3E");
  background-repeat: no-repeat;
  background-position: right 0.5rem center;
  background-size: 1.5em 1.5em;
  transition: all 0.2s ease;
}

.select-dropdown:focus {
  outline: none;
  border-color: #3498DB;
  box-shadow: 0 0 0 3px rgba(52, 152, 219, 0.15);
}

.select-dropdown:hover {
  border-color: #3498DB;
}

/* Style for disabled/placeholder option */
.select-dropdown option[disabled] {
  color: #a0aec0;
}

@media (max-width: 640px) {
  .select-date-box {
    flex-direction: column;
    gap: 0.5rem;
  }
}
</style>
