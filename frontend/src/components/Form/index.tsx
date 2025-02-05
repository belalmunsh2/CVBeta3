// Basic form component shell
// Will implement React Hook Form integration next

import { useForm } from 'react-hook-form';

type FormData = {
  name: string;
  email: string;
  experience: string;
  skills: string;
};

export default function CVForm() {
  const { register, handleSubmit } = useForm<FormData>();

  const onSubmit = (data: FormData) => {
    console.log('Form data:', data);
  };

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <input 
        {...register('name')} 
        placeholder="Full Name"
      />
      <input
        {...register('email')}
        type="email"
        placeholder="Email"
      />
      <textarea
        {...register('experience')}
        placeholder="Work Experience"
      />
      <input
        {...register('skills')}
        placeholder="Key Skills"
      />
      <button type="submit">Generate CV</button>
    </form>
  );
}
