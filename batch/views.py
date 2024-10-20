from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from contract.models import *
from trainer.models import *
from .models import *
from django.contrib import messages


# Create your views here.
@login_required
def batchIndex(request):
    all_batch = Batch.objects.all()
    context = {
        'all_batch':all_batch
    }
    return render(request, 'certificate/batch/index.html', context)


@login_required
def batchCreate(request):
    batch_contract = Contract.objects.all()
    batch_trainer = Trainer.objects.all()

    context = {
        'batch_contract':batch_contract,
        'batch_trainer':batch_trainer
    }
    return render(request, 'certificate/batch/add.html', context)

@login_required
def batchStore(request):
    if request.method == "POST":
        name = request.POST.get('name')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        seats = request.POST.get('seats')
        contract_id = request.POST.get('contract')
        trainers = request.POST.getlist('trainer')

        # Calculate duration
        from datetime import datetime
        start = datetime.strptime(start_date, '%Y-%m-%d')
        end = datetime.strptime(end_date, '%Y-%m-%d')
        delta = end - start
        days = delta.days

        if days < 7:
            duration = f"{days} day{'s' if days > 1 else ''}"
        elif days < 30:
            weeks = days // 7
            duration = f"{weeks} week{'s' if weeks > 1 else ''}"
        else:
            months = days // 30
            duration = f"{months} month{'s' if months > 1 else ''}"

        contract = get_object_or_404(Contract, id=contract_id)
        batch = Batch.objects.create(
            name=name,
            duration=duration,
            start_date=start_date,
            end_date=end_date,
            seats=seats,
            contract=contract
        )

        for trainer_id in trainers:
            trainer = get_object_or_404(Trainer, id=trainer_id)
            batch.trainer.add(trainer)

        messages.success(request, 'Batch successfully created.')
        return redirect('batch-index')
    else:
        messages.error(request, 'Batch cannot be created. Something went wrong!')
    return redirect('batch-create')

@login_required
def batchEdit(request, id):
    edit_batch = get_object_or_404(Batch, id=id)
    batch_contract = Contract.objects.all() 
    batch_trainer = Trainer.objects.all()
    current_trainers = edit_batch.trainer.values_list('id', flat=True)
    context = {
        'edit_batch':edit_batch,
        'batch_contract': batch_contract,
        'batch_trainer': batch_trainer,
        'current_trainers':current_trainers,
    }

    return render(request, 'certificate/batch/edit.html', context)

@login_required
def batchUpdate(request, id):
    update_batch = get_object_or_404(Batch, id=id)

    if request.method == "POST":
        name = request.POST.get('name')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        seats = request.POST.get('seats')
        contract_id = request.POST.get('contract')
        trainers = request.POST.getlist('trainer')

        from datetime import datetime
        start = datetime.strptime(start_date, '%Y-%m-%d')
        end = datetime.strptime(end_date, '%Y-%m-%d')
        delta = end - start
        days = delta.days

        if days < 7:
            duration = f"{days} day{'s' if days > 1 else ''}"
        elif days < 30:
            weeks = days // 7
            duration = f"{weeks} week{'s' if weeks > 1 else ''}"
        else:
            months = days // 30
            duration = f"{months} month{'s' if months > 1 else ''}"

        contract = get_object_or_404(Contract, id=contract_id)
        update_batch.name = name
        update_batch.duration = duration
        update_batch.start_date = start_date
        update_batch.end_date = end_date
        update_batch.seats = seats
        update_batch.contract = contract
        update_batch.save()

        update_batch.trainer.clear() 
        for trainer_id in trainers:
            trainer = get_object_or_404(Trainer, id=trainer_id)
            update_batch.trainer.add(trainer)

        messages.success(request, 'Batch successfully updated.')
        return redirect('batch-index')
    
    else:
        messages.error(request, 'Error while updating the batch !!')
        return redirect('batch-edit')
    

@login_required
def batchDelete(request, id):
    try:
        delete_batch = get_object_or_404(Batch, id=id)
        delete_batch.delete()
        messages.success(request, 'Batch successfully deleted.')
        return redirect('batch-index')
    except:
        messages.error(request, 'Error while deleting the batch !!')
        
    return redirect('batch-index')

