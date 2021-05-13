store = {}
store['timestamp']=1620298845
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py', '--id=26']
store['commit']='2edd2424ec449a84ea20a7324261784a7627b78d'
store['github_url']='2edd2424ec449a84ea20a7324261784a7627b78d'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py'
store['job_id']=26
store['worker_id']=26
store['num_workers']=40
store['config']={'seed': 32, 'acquisition_size': 5, 'max_training_set': 450, 'num_pool_samples': 20, 'num_eval_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'samples_per_epoch': 5056, 'mnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.Random', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationPoolModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 0.0}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples)) + ('OoD Dataset (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastMNIST (test, 10000 samples)'"}
store['initial_training_set_indices']=[30392, 53434, 12640, 8533, 22304, 37915, 58226, 44119, 3091, 14640, 58125, 39579, 43812, 53689, 52296, 46037, 22015, 40334, 57520, 43803]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 2.343252182006836})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.401820659637451})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.957216739654541})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 2.773019313812256})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6847, 'crossentropy': 2.037783984375}
store['active_learning_steps'][0]['acquisition']={'indices': [49803, 42954, 50374, 56556, 34185], 'labels': [-1, -1, -1, 0, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 2.2002921104431152})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.79718017578125})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 3.0045218467712402})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 2.868055820465088})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.6716, 'crossentropy': 2.0217611328125}
store['active_learning_steps'][1]['acquisition']={'indices': [46039, 41471, 59873, 48222, 26245], 'labels': [-1, 3, -1, 9, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.391068935394287})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 2.744682788848877})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.829813241958618})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 3.2826924324035645})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.6683, 'crossentropy': 2.0516390625}
store['active_learning_steps'][2]['acquisition']={'indices': [417, 44532, 53302, 46181, 13210], 'labels': [5, 8, -1, 1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 2.248058319091797})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 2.611997127532959})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 2.681943655014038})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 2.692737579345703})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.7064, 'crossentropy': 1.8332896484375}
store['active_learning_steps'][3]['acquisition']={'indices': [17413, 7409, 10690, 41619, 21657], 'labels': [-1, -1, -1, 3, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.792965292930603})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 2.1977157592773438})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 2.4965596199035645})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 2.58497953414917})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.7117, 'crossentropy': 1.7057046875}
store['active_learning_steps'][4]['acquisition']={'indices': [22900, 5598, 40744, 9776, 24647], 'labels': [-1, 5, 1, 2, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 2.115432024002075})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 2.407362699508667})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 2.503682851791382})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 2.9042515754699707})
store['active_learning_steps'][5]['training']['best_epoch']=1
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.6959, 'crossentropy': 1.9543251953125}
store['active_learning_steps'][5]['acquisition']={'indices': [28716, 37333, 30289, 5733, 4930], 'labels': [3, -1, -1, 2, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.836103916168213})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 2.261240243911743})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 2.4109702110290527})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 2.8295459747314453})
store['active_learning_steps'][6]['training']['best_epoch']=1
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.7064, 'crossentropy': 1.60395234375}
store['active_learning_steps'][6]['acquisition']={'indices': [24085, 43371, 36937, 59224, 34529], 'labels': [-1, 2, 0, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.823663353919983})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 2.338574171066284})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 2.362299680709839})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 2.616666793823242})
store['active_learning_steps'][7]['training']['best_epoch']=1
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.7455, 'crossentropy': 1.65734609375}
store['active_learning_steps'][7]['acquisition']={'indices': [38229, 25676, 24855, 7736, 39307], 'labels': [4, 0, 4, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.797494888305664})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 2.3827767372131348})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 2.2346625328063965})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 2.2586092948913574})
store['active_learning_steps'][8]['training']['best_epoch']=1
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.7369, 'crossentropy': 1.60757158203125}
store['active_learning_steps'][8]['acquisition']={'indices': [1308, 20922, 5231, 32896, 56400], 'labels': [4, 5, 6, 7, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7607421875, 'crossentropy': 1.422278881072998})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7578125, 'crossentropy': 1.8077151775360107})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7509765625, 'crossentropy': 1.9215327501296997})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.76171875, 'crossentropy': 2.0358223915100098})
store['active_learning_steps'][9]['training']['best_epoch']=1
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.7882, 'crossentropy': 1.27899521484375}
store['active_learning_steps'][9]['acquisition']={'indices': [33609, 45620, 4131, 45825, 231], 'labels': [-1, -1, -1, -1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 1.6070153713226318})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.748046875, 'crossentropy': 1.9123347997665405})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.751953125, 'crossentropy': 1.8862406015396118})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.75, 'crossentropy': 2.345897912979126})
store['active_learning_steps'][10]['training']['best_epoch']=1
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.774, 'crossentropy': 1.386601953125}
store['active_learning_steps'][10]['acquisition']={'indices': [1761, 25467, 39433, 11144, 54864], 'labels': [6, -1, 4, 4, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.744140625, 'crossentropy': 1.7030367851257324})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.755859375, 'crossentropy': 1.685064673423767})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.763671875, 'crossentropy': 1.9229624271392822})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7578125, 'crossentropy': 1.9862644672393799})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.775390625, 'crossentropy': 2.0607926845550537})
store['active_learning_steps'][11]['training']['best_epoch']=2
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.7823, 'crossentropy': 1.5384984375}
store['active_learning_steps'][11]['acquisition']={'indices': [10366, 16681, 4638, 58632, 17807], 'labels': [0, 9, -1, 5, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7451171875, 'crossentropy': 1.4485197067260742})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 1.5588839054107666})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.763671875, 'crossentropy': 1.7824516296386719})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.759765625, 'crossentropy': 2.077967882156372})
store['active_learning_steps'][12]['training']['best_epoch']=1
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.7728, 'crossentropy': 1.26443662109375}
store['active_learning_steps'][12]['acquisition']={'indices': [3044, 3151, 24214, 12812, 24199], 'labels': [-1, 7, 6, 3, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 1.4895085096359253})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.7587890625, 'crossentropy': 1.7366881370544434})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.755859375, 'crossentropy': 1.7718427181243896})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 1.9015116691589355})
store['active_learning_steps'][13]['training']['best_epoch']=1
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.783, 'crossentropy': 1.2574419921875}
store['active_learning_steps'][13]['acquisition']={'indices': [28898, 52969, 33368, 8528, 42321], 'labels': [6, -1, 1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7509765625, 'crossentropy': 1.3232537508010864})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7509765625, 'crossentropy': 1.6260707378387451})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.763671875, 'crossentropy': 1.8032400608062744})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.771484375, 'crossentropy': 1.7340220212936401})
store['active_learning_steps'][14]['training']['best_epoch']=1
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.7844, 'crossentropy': 1.23417958984375}
store['active_learning_steps'][14]['acquisition']={'indices': [40611, 28146, 56870, 37150, 18600], 'labels': [0, 4, 1, 9, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.7568359375, 'crossentropy': 1.2414442300796509})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 1.5205386877059937})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 1.5758073329925537})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 1.6177294254302979})
store['active_learning_steps'][15]['training']['best_epoch']=1
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.7873, 'crossentropy': 1.15013408203125}
store['active_learning_steps'][15]['acquisition']={'indices': [48842, 42849, 44159, 50243, 10978], 'labels': [8, -1, 0, -1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.759765625, 'crossentropy': 1.2686856985092163})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.775390625, 'crossentropy': 1.4742052555084229})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 1.5712748765945435})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 1.5955827236175537})
store['active_learning_steps'][16]['training']['best_epoch']=1
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.7866, 'crossentropy': 1.133898828125}
store['active_learning_steps'][16]['acquisition']={'indices': [16296, 32319, 42344, 8616, 21948], 'labels': [3, -1, -1, 7, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.7783203125, 'crossentropy': 1.2390758991241455})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 1.3074591159820557})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 1.7188920974731445})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.791015625, 'crossentropy': 1.475703477859497})
store['active_learning_steps'][17]['training']['best_epoch']=1
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.7909, 'crossentropy': 1.091783203125}
store['active_learning_steps'][17]['acquisition']={'indices': [39528, 17027, 28900, 29244, 51943], 'labels': [6, 8, 3, 2, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 1.1010833978652954})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 1.3433620929718018})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.6112134456634521})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.6481305360794067})
store['active_learning_steps'][18]['training']['best_epoch']=1
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.8145, 'crossentropy': 1.01174853515625}
store['active_learning_steps'][18]['acquisition']={'indices': [55693, 23886, 34512, 5263, 57535], 'labels': [7, 1, 1, 8, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.7763671875, 'crossentropy': 1.2161157131195068})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 1.3524929285049438})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 1.5910416841506958})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 1.6011093854904175})
store['active_learning_steps'][19]['training']['best_epoch']=1
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.7899, 'crossentropy': 1.16192861328125}
store['active_learning_steps'][19]['acquisition']={'indices': [12605, 22423, 42408, 54769, 21513], 'labels': [-1, 9, 8, 4, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.0683438777923584})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 1.2527809143066406})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 1.675383448600769})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 1.6553802490234375})
store['active_learning_steps'][20]['training']['best_epoch']=1
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.8115, 'crossentropy': 1.0075326171875}
store['active_learning_steps'][20]['acquisition']={'indices': [18682, 51102, 51018, 15471, 828], 'labels': [-1, -1, 4, 0, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.052448034286499})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.2609784603118896})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.2436435222625732})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 1.1823194026947021})
store['active_learning_steps'][21]['training']['best_epoch']=1
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.8338, 'crossentropy': 0.97413232421875}
store['active_learning_steps'][21]['acquisition']={'indices': [56070, 20135, 15041, 420, 31070], 'labels': [8, 1, -1, -1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.0369369983673096})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 1.072139859199524})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.1707243919372559})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 1.2180451154708862})
store['active_learning_steps'][22]['training']['best_epoch']=1
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.8311, 'crossentropy': 0.9610177734375}
store['active_learning_steps'][22]['acquisition']={'indices': [22179, 54847, 24883, 24186, 53272], 'labels': [-1, 6, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 0.9842160940170288})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 1.1146881580352783})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 1.2218410968780518})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 1.2853522300720215})
store['active_learning_steps'][23]['training']['best_epoch']=1
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.8146, 'crossentropy': 0.94159921875}
store['active_learning_steps'][23]['acquisition']={'indices': [28258, 19278, 39778, 677, 59829], 'labels': [-1, -1, -1, -1, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 0.9660589694976807})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.035599708557129})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 1.2000057697296143})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 1.2587264776229858})
store['active_learning_steps'][24]['training']['best_epoch']=1
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.8414, 'crossentropy': 0.87916845703125}
store['active_learning_steps'][24]['acquisition']={'indices': [15422, 54493, 4103, 58603, 1449], 'labels': [-1, 3, 8, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.791015625, 'crossentropy': 1.0399664640426636})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 1.192246913909912})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 1.1989805698394775})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 1.2931684255599976})
store['active_learning_steps'][25]['training']['best_epoch']=1
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.8016, 'crossentropy': 1.03501513671875}
store['active_learning_steps'][25]['acquisition']={'indices': [49392, 35073, 362, 39209, 44956], 'labels': [-1, -1, 9, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.9146404266357422})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 1.0741348266601562})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 1.1889408826828003})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 1.2259464263916016})
store['active_learning_steps'][26]['training']['best_epoch']=1
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.8394, 'crossentropy': 0.91883583984375}
store['active_learning_steps'][26]['acquisition']={'indices': [11355, 23895, 55888, 48467, 12435], 'labels': [-1, -1, -1, -1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.1566212177276611})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 1.0736446380615234})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.1974238157272339})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 1.2128006219863892})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 1.2997586727142334})
store['active_learning_steps'][27]['training']['best_epoch']=2
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.8453, 'crossentropy': 0.96347880859375}
store['active_learning_steps'][27]['acquisition']={'indices': [29573, 10493, 31692, 33179, 4140], 'labels': [2, 3, 4, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.0104323625564575})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 1.1130657196044922})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.3299990892410278})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.3773716688156128})
store['active_learning_steps'][28]['training']['best_epoch']=1
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.812, 'crossentropy': 0.9580099609375}
store['active_learning_steps'][28]['acquisition']={'indices': [36058, 16927, 41846, 21911, 6993], 'labels': [9, 3, 4, 2, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 1.0882010459899902})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 1.1353988647460938})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 1.1326758861541748})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.361628770828247})
store['active_learning_steps'][29]['training']['best_epoch']=1
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.8248, 'crossentropy': 0.99740517578125}
store['active_learning_steps'][29]['acquisition']={'indices': [18592, 40260, 2134, 21660, 13574], 'labels': [4, 0, 1, -1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 1.0587033033370972})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.987551212310791})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 1.2358784675598145})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 1.2167233228683472})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 1.4807186126708984})
store['active_learning_steps'][30]['training']['best_epoch']=2
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.8527, 'crossentropy': 0.89444560546875}
store['active_learning_steps'][30]['acquisition']={'indices': [38022, 21677, 22698, 20595, 49457], 'labels': [6, -1, 6, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.9420849680900574})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.1272966861724854})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 1.18265700340271})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.2057080268859863})
store['active_learning_steps'][31]['training']['best_epoch']=1
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.8266, 'crossentropy': 0.87731787109375}
store['active_learning_steps'][31]['acquisition']={'indices': [53908, 39719, 55004, 19585, 40734], 'labels': [1, 2, 4, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 0.9753309488296509})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.9627330303192139})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 1.1377060413360596})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 1.2749406099319458})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.997806191444397})
store['active_learning_steps'][32]['training']['best_epoch']=2
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.8661, 'crossentropy': 0.90150859375}
store['active_learning_steps'][32]['acquisition']={'indices': [24790, 21844, 44519, 57234, 38339], 'labels': [-1, 6, 3, -1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 0.9980407953262329})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 1.0392203330993652})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.135071039199829})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 1.2698901891708374})
store['active_learning_steps'][33]['training']['best_epoch']=1
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.8108, 'crossentropy': 0.96817060546875}
store['active_learning_steps'][33]['acquisition']={'indices': [47634, 28290, 5356, 48549, 11672], 'labels': [-1, 4, 4, 2, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.8855611085891724})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.9472650289535522})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 1.0869556665420532})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 1.1230005025863647})
store['active_learning_steps'][34]['training']['best_epoch']=1
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.845, 'crossentropy': 0.83828486328125}
store['active_learning_steps'][34]['acquisition']={'indices': [50101, 22603, 29234, 30881, 29439], 'labels': [-1, 0, 9, 2, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 1.0818438529968262})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.1732075214385986})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 1.174562931060791})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.3706610202789307})
store['active_learning_steps'][35]['training']['best_epoch']=1
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.8099, 'crossentropy': 1.0101458984375}
store['active_learning_steps'][35]['acquisition']={'indices': [51521, 867, 18352, 24631, 4277], 'labels': [9, 3, 1, 1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.8784838914871216})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.9870965480804443})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 1.006974220275879})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 1.1606957912445068})
store['active_learning_steps'][36]['training']['best_epoch']=1
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.8351, 'crossentropy': 0.84275126953125}
store['active_learning_steps'][36]['acquisition']={'indices': [21372, 6109, 8554, 41575, 15217], 'labels': [-1, -1, 3, -1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.8482319712638855})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.9396077394485474})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 1.0576770305633545})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 1.0407257080078125})
store['active_learning_steps'][37]['training']['best_epoch']=1
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.8521, 'crossentropy': 0.81637900390625}
store['active_learning_steps'][37]['acquisition']={'indices': [41142, 14601, 4887, 12951, 29925], 'labels': [-1, 7, 8, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.9209843873977661})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.9124467372894287})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.93392014503479})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 1.0618956089019775})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 1.1375540494918823})
store['active_learning_steps'][38]['training']['best_epoch']=2
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.8702, 'crossentropy': 0.8453515625}
store['active_learning_steps'][38]['acquisition']={'indices': [59754, 20858, 26934, 12346, 35483], 'labels': [-1, -1, 6, 3, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 0.8945430517196655})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.9289364814758301})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 1.0859293937683105})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 1.084364414215088})
store['active_learning_steps'][39]['training']['best_epoch']=1
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.8493, 'crossentropy': 0.80719482421875}
store['active_learning_steps'][39]['acquisition']={'indices': [15362, 57426, 36643, 1762, 55035], 'labels': [5, 3, -1, 4, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.8650304079055786})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.8902084231376648})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.920468807220459})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.8890222311019897})
store['active_learning_steps'][40]['training']['best_epoch']=1
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.8639, 'crossentropy': 0.767171728515625}
store['active_learning_steps'][40]['acquisition']={'indices': [51983, 36868, 8023, 46850, 10244], 'labels': [2, -1, 5, 1, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 0.9282501339912415})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.924760639667511})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.9172968864440918})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 1.0403268337249756})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 1.01039457321167})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 1.075984001159668})
store['active_learning_steps'][41]['training']['best_epoch']=3
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.8842, 'crossentropy': 0.85995517578125}
store['active_learning_steps'][41]['acquisition']={'indices': [19617, 48402, 28409, 16048, 9655], 'labels': [6, 4, 3, 4, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.8512424230575562})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.8551127910614014})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.9194691181182861})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.8709985017776489})
store['active_learning_steps'][42]['training']['best_epoch']=1
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.8617, 'crossentropy': 0.76634189453125}
store['active_learning_steps'][42]['acquisition']={'indices': [21142, 8921, 57386, 8411, 51019], 'labels': [-1, -1, -1, -1, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 0.9258010387420654})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.9722414612770081})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 1.00676691532135})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.9960108995437622})
store['active_learning_steps'][43]['training']['best_epoch']=1
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.8288, 'crossentropy': 0.84782353515625}
store['active_learning_steps'][43]['acquisition']={'indices': [49706, 1429, 46442, 11704, 43365], 'labels': [-1, -1, 3, 8, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.916601300239563})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.9588476419448853})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.9235361814498901})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.9285176992416382})
store['active_learning_steps'][44]['training']['best_epoch']=1
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.8553, 'crossentropy': 0.805037939453125}
store['active_learning_steps'][44]['acquisition']={'indices': [24792, 52508, 9540, 28825, 53173], 'labels': [5, 0, -1, 3, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.8680232763290405})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.8210675716400146})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.8319779634475708})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 1.0558314323425293})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 1.196249008178711})
store['active_learning_steps'][45]['training']['best_epoch']=2
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.8755, 'crossentropy': 0.743337451171875}
store['active_learning_steps'][45]['acquisition']={'indices': [46933, 44733, 42853, 26593, 28913], 'labels': [-1, -1, 9, 3, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.8870890140533447})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.8673654794692993})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.9709949493408203})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.9969913959503174})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 1.2520544528961182})
store['active_learning_steps'][46]['training']['best_epoch']=2
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.8815, 'crossentropy': 0.794266650390625}
store['active_learning_steps'][46]['acquisition']={'indices': [12448, 41867, 6981, 12349, 21800], 'labels': [-1, -1, 5, 3, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.9037384986877441})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.8982114791870117})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.8987256288528442})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.9945076704025269})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.9502043128013611})
store['active_learning_steps'][47]['training']['best_epoch']=2
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.8827, 'crossentropy': 0.72931904296875}
store['active_learning_steps'][47]['acquisition']={'indices': [19621, 1798, 40795, 30153, 9381], 'labels': [-1, -1, 7, -1, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.8695594668388367})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.788824200630188})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7940365076065063})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.9286227226257324})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 1.0190646648406982})
store['active_learning_steps'][48]['training']['best_epoch']=2
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.8848, 'crossentropy': 0.714750634765625}
store['active_learning_steps'][48]['acquisition']={'indices': [5863, 13411, 29955, 59522, 33897], 'labels': [4, 0, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.8761876821517944})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.8239874839782715})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.8110413551330566})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.8330703973770142})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.9356423616409302})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 1.0303397178649902})
store['active_learning_steps'][49]['training']['best_epoch']=3
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.8972, 'crossentropy': 0.7396296875}
store['active_learning_steps'][49]['acquisition']={'indices': [39288, 48618, 47572, 22113, 54261], 'labels': [-1, -1, -1, 3, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.7895299196243286})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.8748390674591064})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.864022970199585})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.9482302665710449})
store['active_learning_steps'][50]['training']['best_epoch']=1
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.8737, 'crossentropy': 0.722923486328125}
store['active_learning_steps'][50]['acquisition']={'indices': [16015, 51732, 12716, 51948, 19460], 'labels': [7, -1, -1, 8, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.7794634103775024})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.754459023475647})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.8301467895507812})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.9829700589179993})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.9226680994033813})
store['active_learning_steps'][51]['training']['best_epoch']=2
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.8957, 'crossentropy': 0.663335888671875}
store['active_learning_steps'][51]['acquisition']={'indices': [45481, 6644, 9381, 20503, 51527], 'labels': [-1, -1, -1, 6, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.7778662443161011})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7912034392356873})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.8247787952423096})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.8757065534591675})
store['active_learning_steps'][52]['training']['best_epoch']=1
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.8756, 'crossentropy': 0.721532666015625}
store['active_learning_steps'][52]['acquisition']={'indices': [36937, 28862, 30301, 37934, 40084], 'labels': [-1, 1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.9032673835754395})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7663601636886597})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.9889892339706421})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.8323373794555664})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.8784506320953369})
store['active_learning_steps'][53]['training']['best_epoch']=2
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.8991, 'crossentropy': 0.658257666015625}
store['active_learning_steps'][53]['acquisition']={'indices': [38809, 53362, 6156, 12009, 48043], 'labels': [-1, -1, -1, 8, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][54]['training']={}
store['active_learning_steps'][54]['training']['epochs']=[]
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.8710510730743408})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.8104063272476196})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.8520633578300476})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.8862072229385376})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.8676877021789551})
store['active_learning_steps'][54]['training']['best_epoch']=2
store['active_learning_steps'][54]['evaluation_metrics']={'accuracy': 0.8985, 'crossentropy': 0.7216802734375}
store['active_learning_steps'][54]['acquisition']={'indices': [17339, 10921, 82, 4832, 48333], 'labels': [2, 3, -1, 7, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][55]['training']={}
store['active_learning_steps'][55]['training']['epochs']=[]
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.8544267416000366})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7802928686141968})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7174512147903442})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.8714605569839478})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.8186581134796143})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.8884386420249939})
store['active_learning_steps'][55]['training']['best_epoch']=3
store['active_learning_steps'][55]['evaluation_metrics']={'accuracy': 0.8999, 'crossentropy': 0.692781689453125}
store['active_learning_steps'][55]['acquisition']={'indices': [8652, 31521, 57015, 9841, 29124], 'labels': [-1, -1, 6, 2, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][56]['training']={}
store['active_learning_steps'][56]['training']['epochs']=[]
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.8371198177337646})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.7515648603439331})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7965600490570068})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.8146979808807373})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.8560429811477661})
store['active_learning_steps'][56]['training']['best_epoch']=2
store['active_learning_steps'][56]['evaluation_metrics']={'accuracy': 0.9005, 'crossentropy': 0.676762744140625}
store['active_learning_steps'][56]['acquisition']={'indices': [44188, 1704, 45198, 27973, 1937], 'labels': [-1, 4, 4, 8, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][57]['training']={}
store['active_learning_steps'][57]['training']['epochs']=[]
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.8523271083831787})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7675366997718811})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.8298617601394653})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7449758052825928})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.7904517650604248})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.9456555843353271})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.9407210350036621})
store['active_learning_steps'][57]['training']['best_epoch']=4
store['active_learning_steps'][57]['evaluation_metrics']={'accuracy': 0.9082, 'crossentropy': 0.7058701171875}
store['active_learning_steps'][57]['acquisition']={'indices': [45104, 53670, 14339, 18103, 44976], 'labels': [6, -1, 6, 5, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][58]['training']={}
store['active_learning_steps'][58]['training']['epochs']=[]
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.8278636932373047})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.778838038444519})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.8177270889282227})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.8329604864120483})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.87317955493927})
store['active_learning_steps'][58]['training']['best_epoch']=2
store['active_learning_steps'][58]['evaluation_metrics']={'accuracy': 0.891, 'crossentropy': 0.68949892578125}
store['active_learning_steps'][58]['acquisition']={'indices': [54213, 44474, 25959, 6883, 31003], 'labels': [1, 0, 6, 0, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][59]['training']={}
store['active_learning_steps'][59]['training']['epochs']=[]
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.7689365148544312})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7322427034378052})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.8362284302711487})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.85233473777771})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.8648374080657959})
store['active_learning_steps'][59]['training']['best_epoch']=2
store['active_learning_steps'][59]['evaluation_metrics']={'accuracy': 0.9086, 'crossentropy': 0.60975068359375}
store['active_learning_steps'][59]['acquisition']={'indices': [37572, 41030, 20840, 28468, 32022], 'labels': [3, -1, 0, 4, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][60]['training']={}
store['active_learning_steps'][60]['training']['epochs']=[]
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.7133748531341553})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.7600934505462646})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7934563159942627})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.7469137907028198})
store['active_learning_steps'][60]['training']['best_epoch']=1
store['active_learning_steps'][60]['evaluation_metrics']={'accuracy': 0.8878, 'crossentropy': 0.67110234375}
store['active_learning_steps'][60]['acquisition']={'indices': [55645, 12740, 1868, 29148, 8939], 'labels': [-1, -1, 0, -1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][61]['training']={}
store['active_learning_steps'][61]['training']['epochs']=[]
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.7455856800079346})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6949408054351807})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.8253700733184814})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.8435841798782349})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.9172666072845459})
store['active_learning_steps'][61]['training']['best_epoch']=2
store['active_learning_steps'][61]['evaluation_metrics']={'accuracy': 0.9069, 'crossentropy': 0.670196630859375}
store['active_learning_steps'][61]['acquisition']={'indices': [29329, 19112, 12741, 29795, 13485], 'labels': [5, -1, 0, 6, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][62]['training']={}
store['active_learning_steps'][62]['training']['epochs']=[]
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.7439181208610535})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.7306739091873169})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7476301789283752})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.7151843309402466})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.8418652415275574})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.728273332118988})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.859128475189209})
store['active_learning_steps'][62]['training']['best_epoch']=4
store['active_learning_steps'][62]['evaluation_metrics']={'accuracy': 0.9069, 'crossentropy': 0.708532421875}
store['active_learning_steps'][62]['acquisition']={'indices': [17380, 24142, 25751, 25849, 47322], 'labels': [7, 3, 1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][63]['training']={}
store['active_learning_steps'][63]['training']['epochs']=[]
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.7164207100868225})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.7728367447853088})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.8162491917610168})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.8561691045761108})
store['active_learning_steps'][63]['training']['best_epoch']=1
store['active_learning_steps'][63]['evaluation_metrics']={'accuracy': 0.8882, 'crossentropy': 0.650605712890625}
store['active_learning_steps'][63]['acquisition']={'indices': [52906, 36012, 49100, 3148, 38712], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][64]['training']={}
store['active_learning_steps'][64]['training']['epochs']=[]
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.7872041463851929})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7786304950714111})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6814752817153931})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.8852980136871338})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.872803807258606})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.7557315826416016})
store['active_learning_steps'][64]['training']['best_epoch']=3
store['active_learning_steps'][64]['evaluation_metrics']={'accuracy': 0.9092, 'crossentropy': 0.612951025390625}
store['active_learning_steps'][64]['acquisition']={'indices': [8524, 10670, 56573, 28486, 36701], 'labels': [-1, -1, -1, -1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][65]['training']={}
store['active_learning_steps'][65]['training']['epochs']=[]
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.7951148748397827})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.694778323173523})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6998481750488281})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7935065627098083})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.8439643383026123})
store['active_learning_steps'][65]['training']['best_epoch']=2
store['active_learning_steps'][65]['evaluation_metrics']={'accuracy': 0.8956, 'crossentropy': 0.652691259765625}
store['active_learning_steps'][65]['acquisition']={'indices': [53718, 37497, 39408, 27839, 56331], 'labels': [5, -1, -1, 9, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][66]['training']={}
store['active_learning_steps'][66]['training']['epochs']=[]
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7210501432418823})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6682758927345276})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.7102759480476379})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.8023490905761719})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.7361029982566833})
store['active_learning_steps'][66]['training']['best_epoch']=2
store['active_learning_steps'][66]['evaluation_metrics']={'accuracy': 0.9048, 'crossentropy': 0.616266162109375}
store['active_learning_steps'][66]['acquisition']={'indices': [45486, 59716, 42894, 202, 58658], 'labels': [2, 4, -1, 8, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][67]['training']={}
store['active_learning_steps'][67]['training']['epochs']=[]
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.818315327167511})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7736526727676392})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6801150441169739})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.8244805335998535})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.849361777305603})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.8812721967697144})
store['active_learning_steps'][67]['training']['best_epoch']=3
store['active_learning_steps'][67]['evaluation_metrics']={'accuracy': 0.9097, 'crossentropy': 0.61816943359375}
store['active_learning_steps'][67]['acquisition']={'indices': [18321, 35051, 11737, 52650, 36638], 'labels': [-1, 2, -1, 5, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][68]['training']={}
store['active_learning_steps'][68]['training']['epochs']=[]
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.7485792636871338})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6621185541152954})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6706924438476562})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.8134831190109253})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.7913936376571655})
store['active_learning_steps'][68]['training']['best_epoch']=2
store['active_learning_steps'][68]['evaluation_metrics']={'accuracy': 0.9081, 'crossentropy': 0.5866201171875}
store['active_learning_steps'][68]['acquisition']={'indices': [7995, 18131, 36154, 49750, 58232], 'labels': [8, -1, -1, 0, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][69]['training']={}
store['active_learning_steps'][69]['training']['epochs']=[]
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.7501935958862305})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7193915843963623})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.7410306930541992})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.7012125253677368})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6519807577133179})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.7206262946128845})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.7394762635231018})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.726987361907959})
store['active_learning_steps'][69]['training']['best_epoch']=5
store['active_learning_steps'][69]['evaluation_metrics']={'accuracy': 0.9254, 'crossentropy': 0.57619326171875}
store['active_learning_steps'][69]['acquisition']={'indices': [47102, 23675, 16496, 35780, 12166], 'labels': [2, 2, 7, -1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][70]['training']={}
store['active_learning_steps'][70]['training']['epochs']=[]
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.7431858777999878})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.651755690574646})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7044297456741333})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7691537141799927})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.702640950679779})
store['active_learning_steps'][70]['training']['best_epoch']=2
store['active_learning_steps'][70]['evaluation_metrics']={'accuracy': 0.9096, 'crossentropy': 0.589889306640625}
store['active_learning_steps'][70]['acquisition']={'indices': [46869, 28732, 10519, 2628, 4243], 'labels': [6, 5, 1, -1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][71]['training']={}
store['active_learning_steps'][71]['training']['epochs']=[]
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.7879384756088257})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.7558780312538147})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.7995452880859375})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.800101101398468})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.764904260635376})
store['active_learning_steps'][71]['training']['best_epoch']=2
store['active_learning_steps'][71]['evaluation_metrics']={'accuracy': 0.8978, 'crossentropy': 0.693440673828125}
store['active_learning_steps'][71]['acquisition']={'indices': [36359, 58288, 19323, 47776, 59322], 'labels': [4, 3, 1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][72]['training']={}
store['active_learning_steps'][72]['training']['epochs']=[]
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7782911658287048})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6176881194114685})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.682046115398407})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6516665816307068})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.7059096097946167})
store['active_learning_steps'][72]['training']['best_epoch']=2
store['active_learning_steps'][72]['evaluation_metrics']={'accuracy': 0.9004, 'crossentropy': 0.59045966796875}
store['active_learning_steps'][72]['acquisition']={'indices': [34432, 20337, 46331, 9442, 52304], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][73]['training']={}
store['active_learning_steps'][73]['training']['epochs']=[]
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.7634249925613403})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6061627864837646})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6749875545501709})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6853140592575073})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.7379419803619385})
store['active_learning_steps'][73]['training']['best_epoch']=2
store['active_learning_steps'][73]['evaluation_metrics']={'accuracy': 0.9182, 'crossentropy': 0.5319609375}
store['active_learning_steps'][73]['acquisition']={'indices': [50794, 44489, 12040, 34314, 8562], 'labels': [7, -1, 1, 7, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][74]['training']={}
store['active_learning_steps'][74]['training']['epochs']=[]
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.7516735196113586})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7075592279434204})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7108877897262573})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6270222663879395})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.8013695478439331})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.7546314001083374})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.806397557258606})
store['active_learning_steps'][74]['training']['best_epoch']=4
store['active_learning_steps'][74]['evaluation_metrics']={'accuracy': 0.9185, 'crossentropy': 0.592459814453125}
store['active_learning_steps'][74]['acquisition']={'indices': [54433, 48753, 31877, 42693, 48420], 'labels': [0, -1, -1, 2, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][75]['training']={}
store['active_learning_steps'][75]['training']['epochs']=[]
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.7282239198684692})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6839839220046997})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6485072374343872})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.7431879639625549})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7805012464523315})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.7051730751991272})
store['active_learning_steps'][75]['training']['best_epoch']=3
store['active_learning_steps'][75]['evaluation_metrics']={'accuracy': 0.9097, 'crossentropy': 0.586591845703125}
store['active_learning_steps'][75]['acquisition']={'indices': [30695, 38203, 11233, 197, 20724], 'labels': [-1, 4, -1, -1, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][76]['training']={}
store['active_learning_steps'][76]['training']['epochs']=[]
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.743378758430481})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6675610542297363})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7677754163742065})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7492393255233765})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.8431793451309204})
store['active_learning_steps'][76]['training']['best_epoch']=2
store['active_learning_steps'][76]['evaluation_metrics']={'accuracy': 0.9017, 'crossentropy': 0.637832275390625}
store['active_learning_steps'][76]['acquisition']={'indices': [55671, 38693, 13808, 9484, 43204], 'labels': [-1, -1, 0, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][77]['training']={}
store['active_learning_steps'][77]['training']['epochs']=[]
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.7354661822319031})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6603771448135376})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7015026807785034})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7212440371513367})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.728824257850647})
store['active_learning_steps'][77]['training']['best_epoch']=2
store['active_learning_steps'][77]['evaluation_metrics']={'accuracy': 0.9005, 'crossentropy': 0.63989384765625}
store['active_learning_steps'][77]['acquisition']={'indices': [1183, 21786, 15426, 49712, 6197], 'labels': [2, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][78]['training']={}
store['active_learning_steps'][78]['training']['epochs']=[]
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6680748462677002})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6136224865913391})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6194099187850952})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.7166723012924194})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.7457845211029053})
store['active_learning_steps'][78]['training']['best_epoch']=2
store['active_learning_steps'][78]['evaluation_metrics']={'accuracy': 0.9164, 'crossentropy': 0.543813916015625}
store['active_learning_steps'][78]['acquisition']={'indices': [15749, 42236, 34607, 3471, 8836], 'labels': [-1, 4, 3, 3, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][79]['training']={}
store['active_learning_steps'][79]['training']['epochs']=[]
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.6995094418525696})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7084700465202332})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6670809984207153})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.7330306768417358})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6320164203643799})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6644050478935242})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.8548457622528076})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.797756552696228})
store['active_learning_steps'][79]['training']['best_epoch']=5
store['active_learning_steps'][79]['evaluation_metrics']={'accuracy': 0.9198, 'crossentropy': 0.594485302734375}
store['active_learning_steps'][79]['acquisition']={'indices': [22228, 58117, 14967, 54811, 50650], 'labels': [-1, 5, -1, 5, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][80]['training']={}
store['active_learning_steps'][80]['training']['epochs']=[]
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.724532425403595})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6419548988342285})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6387394666671753})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6491395235061646})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.7895787954330444})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6676629781723022})
store['active_learning_steps'][80]['training']['best_epoch']=3
store['active_learning_steps'][80]['evaluation_metrics']={'accuracy': 0.9171, 'crossentropy': 0.55074814453125}
store['active_learning_steps'][80]['acquisition']={'indices': [28207, 9881, 32512, 52973, 29588], 'labels': [7, 0, -1, -1, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][81]['training']={}
store['active_learning_steps'][81]['training']['epochs']=[]
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.7662954926490784})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5812908411026001})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6555441617965698})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6722177267074585})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.7460333108901978})
store['active_learning_steps'][81]['training']['best_epoch']=2
store['active_learning_steps'][81]['evaluation_metrics']={'accuracy': 0.9126, 'crossentropy': 0.523114697265625}
store['active_learning_steps'][81]['acquisition']={'indices': [19222, 3883, 9920, 4418, 58119], 'labels': [-1, 8, -1, -1, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][82]['training']={}
store['active_learning_steps'][82]['training']['epochs']=[]
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.7288103103637695})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6467922925949097})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6751562356948853})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.7305032014846802})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.67529296875})
store['active_learning_steps'][82]['training']['best_epoch']=2
store['active_learning_steps'][82]['evaluation_metrics']={'accuracy': 0.9169, 'crossentropy': 0.55827392578125}
store['active_learning_steps'][82]['acquisition']={'indices': [23476, 43628, 48480, 2640, 50752], 'labels': [6, -1, 3, -1, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][83]['training']={}
store['active_learning_steps'][83]['training']['epochs']=[]
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.8162657022476196})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6940491199493408})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7379555702209473})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6993674635887146})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6980441212654114})
store['active_learning_steps'][83]['training']['best_epoch']=2
store['active_learning_steps'][83]['evaluation_metrics']={'accuracy': 0.9119, 'crossentropy': 0.598570361328125}
store['active_learning_steps'][83]['acquisition']={'indices': [33160, 40318, 13955, 24921, 37723], 'labels': [2, -1, -1, 5, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][84]['training']={}
store['active_learning_steps'][84]['training']['epochs']=[]
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.7560441493988037})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7281148433685303})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.682091474533081})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6914930939674377})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6749695539474487})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.8728435635566711})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.7233564853668213})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.7731379270553589})
store['active_learning_steps'][84]['training']['best_epoch']=5
store['active_learning_steps'][84]['evaluation_metrics']={'accuracy': 0.9267, 'crossentropy': 0.59759248046875}
store['active_learning_steps'][84]['acquisition']={'indices': [40343, 14975, 51292, 15137, 7286], 'labels': [4, 8, -1, -1, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][85]['training']={}
store['active_learning_steps'][85]['training']['epochs']=[]
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.715785026550293})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6550112366676331})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6773511171340942})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.7041137218475342})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6790152788162231})
store['active_learning_steps'][85]['training']['best_epoch']=2
store['active_learning_steps'][85]['evaluation_metrics']={'accuracy': 0.903, 'crossentropy': 0.5913984375}
store['active_learning_steps'][85]['acquisition']={'indices': [40811, 42908, 44366, 26538, 35072], 'labels': [-1, -1, -1, -1, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][86]['training']={}
store['active_learning_steps'][86]['training']['epochs']=[]
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6508570909500122})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5599267482757568})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5835041403770447})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.7014937400817871})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6817028522491455})
store['active_learning_steps'][86]['training']['best_epoch']=2
store['active_learning_steps'][86]['evaluation_metrics']={'accuracy': 0.9139, 'crossentropy': 0.49392099609375}
store['active_learning_steps'][86]['acquisition']={'indices': [11469, 29471, 43209, 16970, 46213], 'labels': [8, 0, -1, 7, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][87]['training']={}
store['active_learning_steps'][87]['training']['epochs']=[]
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.709531307220459})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6466259956359863})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6317700147628784})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.7442653179168701})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.635819673538208})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.7149370908737183})
store['active_learning_steps'][87]['training']['best_epoch']=3
store['active_learning_steps'][87]['evaluation_metrics']={'accuracy': 0.919, 'crossentropy': 0.56307939453125}
store['active_learning_steps'][87]['acquisition']={'indices': [37549, 27653, 31758, 30696, 36707], 'labels': [-1, -1, -1, 9, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][88]['training']={}
store['active_learning_steps'][88]['training']['epochs']=[]
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7068736553192139})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6481157541275024})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6104100942611694})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.617075502872467})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6759088039398193})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.7461574673652649})
store['active_learning_steps'][88]['training']['best_epoch']=3
store['active_learning_steps'][88]['evaluation_metrics']={'accuracy': 0.9193, 'crossentropy': 0.5610919921875}
store['active_learning_steps'][88]['acquisition']={'indices': [34013, 41442, 17955, 57497, 20189], 'labels': [-1, 6, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][89]['training']={}
store['active_learning_steps'][89]['training']['epochs']=[]
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.7027575969696045})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6308963298797607})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.609973669052124})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.7036385536193848})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6401481032371521})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6556130647659302})
store['active_learning_steps'][89]['training']['best_epoch']=3
store['active_learning_steps'][89]['evaluation_metrics']={'accuracy': 0.9218, 'crossentropy': 0.527457861328125}
store['active_learning_steps'][89]['acquisition']={'indices': [40813, 2112, 51205, 58405, 16455], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][90]['training']={}
store['active_learning_steps'][90]['training']['epochs']=[]
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.675532341003418})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6979529857635498})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6698161363601685})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6712596416473389})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.7122498750686646})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7510544061660767})
store['active_learning_steps'][90]['training']['best_epoch']=3
store['active_learning_steps'][90]['evaluation_metrics']={'accuracy': 0.916, 'crossentropy': 0.572013037109375}
store['active_learning_steps'][90]['acquisition']={'indices': [15393, 15131, 36152, 28514, 17723], 'labels': [7, 9, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][91]['training']={}
store['active_learning_steps'][91]['training']['epochs']=[]
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7013429403305054})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5750628709793091})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6478278636932373})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6296701431274414})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.672823429107666})
store['active_learning_steps'][91]['training']['best_epoch']=2
store['active_learning_steps'][91]['evaluation_metrics']={'accuracy': 0.9167, 'crossentropy': 0.510669091796875}
store['active_learning_steps'][91]['acquisition']={'indices': [53714, 31986, 29011, 39483, 55592], 'labels': [1, 9, -1, 0, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][92]['training']={}
store['active_learning_steps'][92]['training']['epochs']=[]
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.7392966747283936})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.659002423286438})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6113578081130981})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6557014584541321})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6466771364212036})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6820546984672546})
store['active_learning_steps'][92]['training']['best_epoch']=3
store['active_learning_steps'][92]['evaluation_metrics']={'accuracy': 0.9247, 'crossentropy': 0.51416455078125}
store['active_learning_steps'][92]['acquisition']={'indices': [14284, 52534, 56542, 41663, 28472], 'labels': [-1, -1, 7, 8, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][93]['training']={}
store['active_learning_steps'][93]['training']['epochs']=[]
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6617758274078369})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6907819509506226})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.7644220590591431})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6446834206581116})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6563159823417664})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6770325899124146})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.7029094696044922})
store['active_learning_steps'][93]['training']['best_epoch']=4
store['active_learning_steps'][93]['evaluation_metrics']={'accuracy': 0.9263, 'crossentropy': 0.577810546875}
store['active_learning_steps'][93]['acquisition']={'indices': [33954, 46740, 14732, 20856, 9710], 'labels': [5, 0, -1, 7, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][94]['training']={}
store['active_learning_steps'][94]['training']['epochs']=[]
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7434186935424805})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6010931730270386})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6532472372055054})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6730634570121765})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6257928609848022})
store['active_learning_steps'][94]['training']['best_epoch']=2
store['active_learning_steps'][94]['evaluation_metrics']={'accuracy': 0.9116, 'crossentropy': 0.56551533203125}
store['active_learning_steps'][94]['acquisition']={'indices': [31561, 50372, 55320, 43209, 14205], 'labels': [9, 3, 4, 3, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][95]['training']={}
store['active_learning_steps'][95]['training']['epochs']=[]
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.7787193059921265})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.630544900894165})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5772138237953186})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6264992952346802})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6522119045257568})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6210941076278687})
store['active_learning_steps'][95]['training']['best_epoch']=3
store['active_learning_steps'][95]['evaluation_metrics']={'accuracy': 0.9213, 'crossentropy': 0.53282021484375}
store['active_learning_steps'][95]['acquisition']={'indices': [20874, 31049, 46321, 35546, 38294], 'labels': [2, 3, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][96]['training']={}
store['active_learning_steps'][96]['training']['epochs']=[]
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.699612021446228})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6895076036453247})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6046850681304932})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6751120090484619})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.7046982049942017})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6941480040550232})
store['active_learning_steps'][96]['training']['best_epoch']=3
store['active_learning_steps'][96]['evaluation_metrics']={'accuracy': 0.9197, 'crossentropy': 0.51059658203125}
store['active_learning_steps'][96]['acquisition']={'indices': [27355, 53688, 24194, 15347, 44109], 'labels': [-1, -1, 9, 4, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][97]['training']={}
store['active_learning_steps'][97]['training']['epochs']=[]
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7265374660491943})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6411725878715515})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6662840247154236})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6852131485939026})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.7284794449806213})
store['active_learning_steps'][97]['training']['best_epoch']=2
store['active_learning_steps'][97]['evaluation_metrics']={'accuracy': 0.9186, 'crossentropy': 0.544415234375}
store['active_learning_steps'][97]['acquisition']={'indices': [11234, 17535, 39897, 55699, 8830], 'labels': [3, 0, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][98]['training']={}
store['active_learning_steps'][98]['training']['epochs']=[]
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.7441533803939819})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6144551634788513})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5633080005645752})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.613044023513794})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6799395084381104})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6513155698776245})
store['active_learning_steps'][98]['training']['best_epoch']=3
store['active_learning_steps'][98]['evaluation_metrics']={'accuracy': 0.926, 'crossentropy': 0.498692822265625}
store['active_learning_steps'][98]['acquisition']={'indices': [12978, 39263, 59082, 13998, 7049], 'labels': [-1, 0, 7, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][99]['training']={}
store['active_learning_steps'][99]['training']['epochs']=[]
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6824126243591309})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6094130277633667})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6205514669418335})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6274247169494629})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.715681791305542})
store['active_learning_steps'][99]['training']['best_epoch']=2
store['active_learning_steps'][99]['evaluation_metrics']={'accuracy': 0.9102, 'crossentropy': 0.54334521484375}
store['active_learning_steps'][99]['acquisition']={'indices': [28518, 54373, 35417, 35260, 25365], 'labels': [4, 1, 7, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][100]['training']={}
store['active_learning_steps'][100]['training']['epochs']=[]
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.7153140306472778})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6617961525917053})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6551711559295654})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.576877236366272})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5800299644470215})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.6738821268081665})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.7660280466079712})
store['active_learning_steps'][100]['training']['best_epoch']=4
store['active_learning_steps'][100]['evaluation_metrics']={'accuracy': 0.9301, 'crossentropy': 0.492407568359375}
store['active_learning_steps'][100]['acquisition']={'indices': [1754, 52026, 56325, 41552, 728], 'labels': [2, -1, -1, -1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][101]['training']={}
store['active_learning_steps'][101]['training']['epochs']=[]
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.7088855504989624})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5425308346748352})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.601834774017334})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5716457366943359})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6287456750869751})
store['active_learning_steps'][101]['training']['best_epoch']=2
store['active_learning_steps'][101]['evaluation_metrics']={'accuracy': 0.9186, 'crossentropy': 0.518115869140625}
store['active_learning_steps'][101]['acquisition']={'indices': [32869, 31654, 44002, 8163, 31025], 'labels': [0, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][102]['training']={}
store['active_learning_steps'][102]['training']['epochs']=[]
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.8393753170967102})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6174808740615845})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6194031834602356})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6178461313247681})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6589748859405518})
store['active_learning_steps'][102]['training']['best_epoch']=2
store['active_learning_steps'][102]['evaluation_metrics']={'accuracy': 0.908, 'crossentropy': 0.5756265625}
store['active_learning_steps'][102]['acquisition']={'indices': [27785, 5191, 38720, 26131, 29891], 'labels': [-1, 2, -1, -1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][103]['training']={}
store['active_learning_steps'][103]['training']['epochs']=[]
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.6995612382888794})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5964441299438477})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7133455276489258})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.647559642791748})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.7084344625473022})
store['active_learning_steps'][103]['training']['best_epoch']=2
store['active_learning_steps'][103]['evaluation_metrics']={'accuracy': 0.9125, 'crossentropy': 0.53218896484375}
store['active_learning_steps'][103]['acquisition']={'indices': [885, 59533, 24190, 9187, 527], 'labels': [-1, -1, 8, -1, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][104]['training']={}
store['active_learning_steps'][104]['training']['epochs']=[]
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6826654076576233})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6135202050209045})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6478828191757202})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.623726487159729})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6185383796691895})
store['active_learning_steps'][104]['training']['best_epoch']=2
store['active_learning_steps'][104]['evaluation_metrics']={'accuracy': 0.9158, 'crossentropy': 0.525601025390625}
store['active_learning_steps'][104]['acquisition']={'indices': [5363, 50142, 19451, 20642, 17405], 'labels': [5, 5, 6, -1, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][105]['training']={}
store['active_learning_steps'][105]['training']['epochs']=[]
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6656268835067749})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5862876176834106})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.594383955001831})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6221314668655396})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6580994129180908})
store['active_learning_steps'][105]['training']['best_epoch']=2
store['active_learning_steps'][105]['evaluation_metrics']={'accuracy': 0.9159, 'crossentropy': 0.551302685546875}
store['active_learning_steps'][105]['acquisition']={'indices': [9722, 26246, 22663, 18752, 58866], 'labels': [-1, 4, 3, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][106]['training']={}
store['active_learning_steps'][106]['training']['epochs']=[]
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.6552487015724182})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6033846139907837})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6185986995697021})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5883262753486633})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6561450958251953})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6286329627037048})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6347640156745911})
store['active_learning_steps'][106]['training']['best_epoch']=4
store['active_learning_steps'][106]['evaluation_metrics']={'accuracy': 0.927, 'crossentropy': 0.52064189453125}
store['active_learning_steps'][106]['acquisition']={'indices': [28577, 3224, 21737, 13917, 9816], 'labels': [-1, -1, 1, 8, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][107]['training']={}
store['active_learning_steps'][107]['training']['epochs']=[]
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.7526863813400269})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5658633708953857})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5959476232528687})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6232356429100037})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6112604141235352})
store['active_learning_steps'][107]['training']['best_epoch']=2
store['active_learning_steps'][107]['evaluation_metrics']={'accuracy': 0.9109, 'crossentropy': 0.528490673828125}
store['active_learning_steps'][107]['acquisition']={'indices': [40756, 2455, 25526, 9224, 5196], 'labels': [5, 7, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][108]['training']={}
store['active_learning_steps'][108]['training']['epochs']=[]
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7580544948577881})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6499687433242798})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5667203664779663})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6729047298431396})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6775814890861511})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6481219530105591})
store['active_learning_steps'][108]['training']['best_epoch']=3
store['active_learning_steps'][108]['evaluation_metrics']={'accuracy': 0.9248, 'crossentropy': 0.548363671875}
store['active_learning_steps'][108]['acquisition']={'indices': [53428, 33594, 48946, 19581, 14487], 'labels': [-1, -1, 2, -1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][109]['training']={}
store['active_learning_steps'][109]['training']['epochs']=[]
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.6879395246505737})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5906385183334351})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6619446873664856})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6154360771179199})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6161737442016602})
store['active_learning_steps'][109]['training']['best_epoch']=2
store['active_learning_steps'][109]['evaluation_metrics']={'accuracy': 0.9094, 'crossentropy': 0.56675048828125}
store['active_learning_steps'][109]['acquisition']={'indices': [14673, 39078, 23609, 26923, 2932], 'labels': [5, -1, 7, -1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][110]['training']={}
store['active_learning_steps'][110]['training']['epochs']=[]
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.590103268623352})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5779081583023071})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5678760409355164})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5385499000549316})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.6235402822494507})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.659510612487793})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6609047651290894})
store['active_learning_steps'][110]['training']['best_epoch']=4
store['active_learning_steps'][110]['evaluation_metrics']={'accuracy': 0.9285, 'crossentropy': 0.498265576171875}
store['active_learning_steps'][110]['acquisition']={'indices': [27826, 48796, 49519, 38049, 27075], 'labels': [4, 8, -1, 3, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][111]['training']={}
store['active_learning_steps'][111]['training']['epochs']=[]
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6539946794509888})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6216083765029907})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.617613673210144})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6101548671722412})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6474945545196533})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5812442302703857})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5987980961799622})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6406291127204895})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.6180524826049805})
store['active_learning_steps'][111]['training']['best_epoch']=6
store['active_learning_steps'][111]['evaluation_metrics']={'accuracy': 0.9304, 'crossentropy': 0.541461962890625}
store['active_learning_steps'][111]['acquisition']={'indices': [22477, 2112, 42511, 26445, 45074], 'labels': [-1, -1, 5, 1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][112]['training']={}
store['active_learning_steps'][112]['training']['epochs']=[]
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.6771267652511597})
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6150977611541748})
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5797185897827148})
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6163328886032104})
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6425436735153198})
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.7201574444770813})
store['active_learning_steps'][112]['training']['best_epoch']=3
store['active_learning_steps'][112]['evaluation_metrics']={'accuracy': 0.9255, 'crossentropy': 0.4804126953125}
store['active_learning_steps'][112]['acquisition']={'indices': [5932, 19250, 26327, 11881, 32263], 'labels': [0, -1, 8, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][113]['training']={}
store['active_learning_steps'][113]['training']['epochs']=[]
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.6715039014816284})
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6260279417037964})
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6455085277557373})
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6267858743667603})
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.7007544040679932})
store['active_learning_steps'][113]['training']['best_epoch']=2
store['active_learning_steps'][113]['evaluation_metrics']={'accuracy': 0.9102, 'crossentropy': 0.54727294921875}
store['active_learning_steps'][113]['acquisition']={'indices': [59044, 3237, 54435, 34651, 13129], 'labels': [1, -1, 7, 9, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][114]['training']={}
store['active_learning_steps'][114]['training']['epochs']=[]
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6379696726799011})
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5449038743972778})
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5618207454681396})
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5764981508255005})
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5924577713012695})
store['active_learning_steps'][114]['training']['best_epoch']=2
store['active_learning_steps'][114]['evaluation_metrics']={'accuracy': 0.9181, 'crossentropy': 0.507948046875}
store['active_learning_steps'][114]['acquisition']={'indices': [7608, 43083, 41151, 38450, 49275], 'labels': [7, -1, 7, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][115]['training']={}
store['active_learning_steps'][115]['training']['epochs']=[]
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.66493821144104})
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.562536358833313})
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5837980508804321})
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6008223295211792})
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.615803062915802})
store['active_learning_steps'][115]['training']['best_epoch']=2
store['active_learning_steps'][115]['evaluation_metrics']={'accuracy': 0.9175, 'crossentropy': 0.518404248046875}
store['active_learning_steps'][115]['acquisition']={'indices': [50818, 54978, 4107, 56274, 58895], 'labels': [-1, 2, -1, -1, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][116]['training']={}
store['active_learning_steps'][116]['training']['epochs']=[]
store['active_learning_steps'][116]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6920900344848633})
store['active_learning_steps'][116]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5510714054107666})
store['active_learning_steps'][116]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5762848854064941})
store['active_learning_steps'][116]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5565942525863647})
store['active_learning_steps'][116]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6609333753585815})
store['active_learning_steps'][116]['training']['best_epoch']=2
store['active_learning_steps'][116]['evaluation_metrics']={'accuracy': 0.9132, 'crossentropy': 0.543126220703125}
store['active_learning_steps'][116]['acquisition']={'indices': [58203, 14162, 676, 40226, 1274], 'labels': [-1, -1, 1, 4, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][117]['training']={}
store['active_learning_steps'][117]['training']['epochs']=[]
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.7157930135726929})
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6261007189750671})
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5411484241485596})
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6293886303901672})
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6584959030151367})
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.605815052986145})
store['active_learning_steps'][117]['training']['best_epoch']=3
store['active_learning_steps'][117]['evaluation_metrics']={'accuracy': 0.9286, 'crossentropy': 0.48856630859375}
store['active_learning_steps'][117]['acquisition']={'indices': [20651, 41454, 44886, 36119, 53516], 'labels': [4, 1, -1, -1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][118]['training']={}
store['active_learning_steps'][118]['training']['epochs']=[]
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.6875056624412537})
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6058404445648193})
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5654534101486206})
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5719996690750122})
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.6318268179893494})
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5554203391075134})
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.601032018661499})
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.648547887802124})
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.6077170968055725})
store['active_learning_steps'][118]['training']['best_epoch']=6
store['active_learning_steps'][118]['evaluation_metrics']={'accuracy': 0.9283, 'crossentropy': 0.55372734375}
store['active_learning_steps'][118]['acquisition']={'indices': [21948, 44673, 8634, 14924, 57222], 'labels': [-1, 5, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][119]['training']={}
store['active_learning_steps'][119]['training']['epochs']=[]
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6500672101974487})
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.590040922164917})
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6006748676300049})
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6220965385437012})
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5429383516311646})
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.631615161895752})
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6738390922546387})
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.639089822769165})
store['active_learning_steps'][119]['training']['best_epoch']=5
store['active_learning_steps'][119]['evaluation_metrics']={'accuracy': 0.931, 'crossentropy': 0.535136865234375}
store['active_learning_steps'][119]['acquisition']={'indices': [29047, 45021, 36797, 15707, 55701], 'labels': [-1, 0, -1, 8, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][120]['training']={}
store['active_learning_steps'][120]['training']['epochs']=[]
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7048240303993225})
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5850818157196045})
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6615352630615234})
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5054214000701904})
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5523208379745483})
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6430137753486633})
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6223868131637573})
store['active_learning_steps'][120]['training']['best_epoch']=4
store['active_learning_steps'][120]['evaluation_metrics']={'accuracy': 0.9322, 'crossentropy': 0.469046484375}
store['active_learning_steps'][120]['acquisition']={'indices': [44142, 23738, 40486, 4574, 11793], 'labels': [-1, 9, 0, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][121]['training']={}
store['active_learning_steps'][121]['training']['epochs']=[]
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6542366743087769})
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5438200235366821})
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5835633873939514})
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6344479322433472})
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5887435674667358})
store['active_learning_steps'][121]['training']['best_epoch']=2
store['active_learning_steps'][121]['evaluation_metrics']={'accuracy': 0.919, 'crossentropy': 0.497934716796875}
store['active_learning_steps'][121]['acquisition']={'indices': [56872, 53380, 13326, 11360, 34613], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][122]['training']={}
store['active_learning_steps'][122]['training']['epochs']=[]
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7129456996917725})
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5734509229660034})
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5584072470664978})
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5861138105392456})
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6258078217506409})
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5784382820129395})
store['active_learning_steps'][122]['training']['best_epoch']=3
store['active_learning_steps'][122]['evaluation_metrics']={'accuracy': 0.917, 'crossentropy': 0.5341263671875}
store['active_learning_steps'][122]['acquisition']={'indices': [32787, 9177, 36727, 5192, 4925], 'labels': [-1, -1, 8, 0, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][123]['training']={}
store['active_learning_steps'][123]['training']['epochs']=[]
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6757683753967285})
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5587747097015381})
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5647004842758179})
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5991507768630981})
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6324775218963623})
store['active_learning_steps'][123]['training']['best_epoch']=2
store['active_learning_steps'][123]['evaluation_metrics']={'accuracy': 0.9163, 'crossentropy': 0.49374912109375}
store['active_learning_steps'][123]['acquisition']={'indices': [59841, 43318, 3930, 58034, 58560], 'labels': [-1, -1, -1, 9, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][124]['training']={}
store['active_learning_steps'][124]['training']['epochs']=[]
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.6723625659942627})
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5061172246932983})
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.49280405044555664})
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5379000902175903})
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5465036630630493})
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.6019036769866943})
store['active_learning_steps'][124]['training']['best_epoch']=3
store['active_learning_steps'][124]['evaluation_metrics']={'accuracy': 0.929, 'crossentropy': 0.467805419921875}
store['active_learning_steps'][124]['acquisition']={'indices': [41303, 39507, 54110, 39237, 20339], 'labels': [6, 2, -1, 1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][125]['training']={}
store['active_learning_steps'][125]['training']['epochs']=[]
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6681493520736694})
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5681589841842651})
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5789197683334351})
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5610443353652954})
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5612804293632507})
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6797033548355103})
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.636252224445343})
store['active_learning_steps'][125]['training']['best_epoch']=4
store['active_learning_steps'][125]['evaluation_metrics']={'accuracy': 0.9312, 'crossentropy': 0.4936146484375}
store['active_learning_steps'][125]['acquisition']={'indices': [10716, 13320, 4501, 43799, 48213], 'labels': [7, -1, -1, -1, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][126]['training']={}
store['active_learning_steps'][126]['training']['epochs']=[]
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6414405703544617})
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6034026145935059})
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5026050209999084})
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5492941737174988})
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6061022281646729})
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5915201306343079})
store['active_learning_steps'][126]['training']['best_epoch']=3
store['active_learning_steps'][126]['evaluation_metrics']={'accuracy': 0.9279, 'crossentropy': 0.468059619140625}
store['active_learning_steps'][126]['acquisition']={'indices': [21136, 19845, 24212, 50401, 23011], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][127]['training']={}
store['active_learning_steps'][127]['training']['epochs']=[]
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.7343419790267944})
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5682779550552368})
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5531556010246277})
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5377966165542603})
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5949636697769165})
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6050029397010803})
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5873720049858093})
store['active_learning_steps'][127]['training']['best_epoch']=4
store['active_learning_steps'][127]['evaluation_metrics']={'accuracy': 0.9277, 'crossentropy': 0.490760791015625}
store['active_learning_steps'][127]['acquisition']={'indices': [44516, 52409, 50381, 35106, 14856], 'labels': [7, -1, 2, 2, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][128]['training']={}
store['active_learning_steps'][128]['training']['epochs']=[]
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6446008682250977})
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5576956868171692})
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5361608266830444})
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5200935006141663})
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5475152730941772})
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.607648491859436})
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6445789337158203})
store['active_learning_steps'][128]['training']['best_epoch']=4
store['active_learning_steps'][128]['evaluation_metrics']={'accuracy': 0.9314, 'crossentropy': 0.47935419921875}
store['active_learning_steps'][128]['acquisition']={'indices': [48697, 3627, 12519, 31882, 57396], 'labels': [1, 2, -1, 7, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][129]['training']={}
store['active_learning_steps'][129]['training']['epochs']=[]
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.6999746561050415})
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5827945470809937})
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.553826093673706})
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.513394832611084})
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5311788320541382})
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5493745803833008})
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5697612166404724})
store['active_learning_steps'][129]['training']['best_epoch']=4
store['active_learning_steps'][129]['evaluation_metrics']={'accuracy': 0.9342, 'crossentropy': 0.448595751953125}
store['active_learning_steps'][129]['acquisition']={'indices': [6590, 45008, 49939, 57949, 33394], 'labels': [7, -1, 0, 7, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][130]['training']={}
store['active_learning_steps'][130]['training']['epochs']=[]
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.642927348613739})
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5040549039840698})
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5515996217727661})
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5714468955993652})
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5480511784553528})
store['active_learning_steps'][130]['training']['best_epoch']=2
store['active_learning_steps'][130]['evaluation_metrics']={'accuracy': 0.9269, 'crossentropy': 0.45683974609375}
store['active_learning_steps'][130]['acquisition']={'indices': [48566, 55740, 10940, 56595, 7772], 'labels': [-1, -1, 7, 4, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][131]['training']={}
store['active_learning_steps'][131]['training']['epochs']=[]
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.6966061592102051})
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.637119472026825})
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5669276118278503})
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5466924905776978})
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5352129936218262})
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5289249420166016})
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5362452268600464})
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5605695247650146})
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.6095564365386963})
store['active_learning_steps'][131]['training']['best_epoch']=6
store['active_learning_steps'][131]['evaluation_metrics']={'accuracy': 0.9321, 'crossentropy': 0.505717822265625}
store['active_learning_steps'][131]['acquisition']={'indices': [59447, 38736, 19211, 29258, 47], 'labels': [8, 1, 1, 4, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][132]['training']={}
store['active_learning_steps'][132]['training']['epochs']=[]
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.701741635799408})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5279661417007446})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5099289417266846})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5535237193107605})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5198349356651306})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5743794441223145})
store['active_learning_steps'][132]['training']['best_epoch']=3
store['active_learning_steps'][132]['evaluation_metrics']={'accuracy': 0.9226, 'crossentropy': 0.46024013671875}
store['active_learning_steps'][132]['acquisition']={'indices': [25884, 41922, 38283, 17878, 42358], 'labels': [-1, -1, -1, 8, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][133]['training']={}
store['active_learning_steps'][133]['training']['epochs']=[]
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.673599123954773})
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.526218056678772})
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5183078050613403})
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6156167387962341})
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5813337564468384})
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6180071234703064})
store['active_learning_steps'][133]['training']['best_epoch']=3
store['active_learning_steps'][133]['evaluation_metrics']={'accuracy': 0.9266, 'crossentropy': 0.475028955078125}
store['active_learning_steps'][133]['acquisition']={'indices': [5928, 30577, 32362, 58524, 37071], 'labels': [-1, 6, -1, -1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][134]['training']={}
store['active_learning_steps'][134]['training']['epochs']=[]
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6676534414291382})
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5313187837600708})
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5096919536590576})
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5047445297241211})
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5236009359359741})
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5428091287612915})
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5863062739372253})
store['active_learning_steps'][134]['training']['best_epoch']=4
store['active_learning_steps'][134]['evaluation_metrics']={'accuracy': 0.9308, 'crossentropy': 0.453458447265625}
store['active_learning_steps'][134]['acquisition']={'indices': [39726, 46542, 27597, 19010, 46451], 'labels': [2, 1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][135]['training']={}
store['active_learning_steps'][135]['training']['epochs']=[]
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.7074519991874695})
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.4721478223800659})
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5267186164855957})
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5201083421707153})
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5328852534294128})
store['active_learning_steps'][135]['training']['best_epoch']=2
store['active_learning_steps'][135]['evaluation_metrics']={'accuracy': 0.9211, 'crossentropy': 0.46185888671875}
store['active_learning_steps'][135]['acquisition']={'indices': [24216, 8523, 31707, 11728, 54414], 'labels': [-1, 6, 9, -1, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][136]['training']={}
store['active_learning_steps'][136]['training']['epochs']=[]
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6558727025985718})
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.557435154914856})
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5251769423484802})
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5008856058120728})
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5261479616165161})
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5665631890296936})
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5462458729743958})
store['active_learning_steps'][136]['training']['best_epoch']=4
store['active_learning_steps'][136]['evaluation_metrics']={'accuracy': 0.9349, 'crossentropy': 0.4352396484375}
store['active_learning_steps'][136]['acquisition']={'indices': [31806, 32465, 22886, 17697, 4011], 'labels': [-1, 1, -1, 2, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][137]['training']={}
store['active_learning_steps'][137]['training']['epochs']=[]
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6772923469543457})
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.4859931766986847})
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4418078064918518})
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4399911165237427})
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4676526188850403})
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.49471914768218994})
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5285217761993408})
store['active_learning_steps'][137]['training']['best_epoch']=4
store['active_learning_steps'][137]['evaluation_metrics']={'accuracy': 0.9375, 'crossentropy': 0.415787939453125}
store['active_learning_steps'][137]['acquisition']={'indices': [9626, 25233, 20751, 56571, 29186], 'labels': [4, 9, 0, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][138]['training']={}
store['active_learning_steps'][138]['training']['epochs']=[]
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.6978567838668823})
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5455155372619629})
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.49529099464416504})
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5153283476829529})
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5553169846534729})
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.6303121447563171})
store['active_learning_steps'][138]['training']['best_epoch']=3
store['active_learning_steps'][138]['evaluation_metrics']={'accuracy': 0.9349, 'crossentropy': 0.427019140625}
store['active_learning_steps'][138]['acquisition']={'indices': [33553, 53868, 48227, 27838, 56237], 'labels': [-1, -1, -1, -1, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][139]['training']={}
store['active_learning_steps'][139]['training']['epochs']=[]
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6335726976394653})
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5092649459838867})
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.48249977827072144})
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5365723371505737})
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5192915797233582})
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5050737261772156})
store['active_learning_steps'][139]['training']['best_epoch']=3
store['active_learning_steps'][139]['evaluation_metrics']={'accuracy': 0.9305, 'crossentropy': 0.432336328125}
store['active_learning_steps'][139]['acquisition']={'indices': [52033, 2789, 19960, 48682, 19921], 'labels': [8, -1, -1, 3, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][140]['training']={}
store['active_learning_steps'][140]['training']['epochs']=[]
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.7042138576507568})
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5266600847244263})
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6123729348182678})
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5469841361045837})
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5226468443870544})
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.602209210395813})
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5718107223510742})
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5562515258789062})
store['active_learning_steps'][140]['training']['best_epoch']=5
store['active_learning_steps'][140]['evaluation_metrics']={'accuracy': 0.9394, 'crossentropy': 0.425671728515625}
store['active_learning_steps'][140]['acquisition']={'indices': [32594, 22564, 37295, 3058, 30998], 'labels': [-1, 4, 4, 6, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][141]['training']={}
store['active_learning_steps'][141]['training']['epochs']=[]
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.7225015163421631})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5340613126754761})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5210046768188477})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5094211101531982})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5507247447967529})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.578863799571991})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5893334150314331})
store['active_learning_steps'][141]['training']['best_epoch']=4
store['active_learning_steps'][141]['evaluation_metrics']={'accuracy': 0.9385, 'crossentropy': 0.43315830078125}
store['active_learning_steps'][141]['acquisition']={'indices': [22730, 17027, 59146, 49118, 6882], 'labels': [3, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][142]['training']={}
store['active_learning_steps'][142]['training']['epochs']=[]
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.6926795244216919})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.49666285514831543})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5058062672615051})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5161358118057251})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5504825115203857})
store['active_learning_steps'][142]['training']['best_epoch']=2
store['active_learning_steps'][142]['evaluation_metrics']={'accuracy': 0.9242, 'crossentropy': 0.453249169921875}
store['active_learning_steps'][142]['acquisition']={'indices': [51635, 13318, 21172, 15419, 10376], 'labels': [-1, -1, -1, 6, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][143]['training']={}
store['active_learning_steps'][143]['training']['epochs']=[]
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6484664082527161})
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.529024600982666})
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5525227785110474})
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.49450063705444336})
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4898194670677185})
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5749240517616272})
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.49552470445632935})
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5899478197097778})
store['active_learning_steps'][143]['training']['best_epoch']=5
store['active_learning_steps'][143]['evaluation_metrics']={'accuracy': 0.9406, 'crossentropy': 0.420489599609375}
store['active_learning_steps'][143]['acquisition']={'indices': [46549, 43790, 50032, 16714, 47159], 'labels': [3, 1, 1, 1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][144]['training']={}
store['active_learning_steps'][144]['training']['epochs']=[]
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6403363943099976})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5465476512908936})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5785985589027405})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5386970043182373})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6019587516784668})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6129584312438965})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.619476854801178})
store['active_learning_steps'][144]['training']['best_epoch']=4
store['active_learning_steps'][144]['evaluation_metrics']={'accuracy': 0.9382, 'crossentropy': 0.43183916015625}
store['active_learning_steps'][144]['acquisition']={'indices': [11464, 33684, 31244, 56064, 57324], 'labels': [-1, -1, -1, 7, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][145]['training']={}
store['active_learning_steps'][145]['training']['epochs']=[]
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6482977867126465})
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5320369601249695})
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5050382614135742})
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5685619115829468})
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5152968168258667})
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5472068786621094})
store['active_learning_steps'][145]['training']['best_epoch']=3
store['active_learning_steps'][145]['evaluation_metrics']={'accuracy': 0.9391, 'crossentropy': 0.415133740234375}
store['active_learning_steps'][145]['acquisition']={'indices': [26340, 57563, 9254, 51365, 11037], 'labels': [-1, -1, 6, -1, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][146]['training']={}
store['active_learning_steps'][146]['training']['epochs']=[]
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6763508319854736})
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.5891914367675781})
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6038085222244263})
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5653738975524902})
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5600446462631226})
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5617377758026123})
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5879136919975281})
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.6354217529296875})
store['active_learning_steps'][146]['training']['best_epoch']=5
store['active_learning_steps'][146]['evaluation_metrics']={'accuracy': 0.9384, 'crossentropy': 0.446682470703125}
store['active_learning_steps'][146]['acquisition']={'indices': [49147, 42013, 16265, 30554, 21839], 'labels': [-1, 9, -1, 4, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][147]['training']={}
store['active_learning_steps'][147]['training']['epochs']=[]
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.617583692073822})
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5081733465194702})
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.516791582107544})
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5729525089263916})
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5813726782798767})
store['active_learning_steps'][147]['training']['best_epoch']=2
store['active_learning_steps'][147]['evaluation_metrics']={'accuracy': 0.9279, 'crossentropy': 0.457592236328125}
store['active_learning_steps'][147]['acquisition']={'indices': [11394, 52158, 34233, 4954, 16884], 'labels': [2, -1, -1, 4, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][148]['training']={}
store['active_learning_steps'][148]['training']['epochs']=[]
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.7210531234741211})
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5383586883544922})
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5512248873710632})
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5178940892219543})
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6034001111984253})
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5412887334823608})
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6473115682601929})
store['active_learning_steps'][148]['training']['best_epoch']=4
store['active_learning_steps'][148]['evaluation_metrics']={'accuracy': 0.9291, 'crossentropy': 0.4465259765625}
store['active_learning_steps'][148]['acquisition']={'indices': [34218, 7180, 19213, 10856, 30638], 'labels': [-1, 9, 2, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][149]['training']={}
store['active_learning_steps'][149]['training']['epochs']=[]
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6888210773468018})
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5554311275482178})
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5384935140609741})
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.548681378364563})
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5583842992782593})
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5915641784667969})
store['active_learning_steps'][149]['training']['best_epoch']=3
store['active_learning_steps'][149]['evaluation_metrics']={'accuracy': 0.9263, 'crossentropy': 0.46142431640625}
store['active_learning_steps'][149]['acquisition']={'indices': [9990, 54676, 31948, 30873, 53349], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][150]['training']={}
store['active_learning_steps'][150]['training']['epochs']=[]
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7022842168807983})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.524588942527771})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5293512344360352})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.541429340839386})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4730060398578644})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5871800184249878})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5245441794395447})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5537267327308655})
store['active_learning_steps'][150]['training']['best_epoch']=5
store['active_learning_steps'][150]['evaluation_metrics']={'accuracy': 0.9439, 'crossentropy': 0.3928843017578125}
store['active_learning_steps'][150]['acquisition']={'indices': [5772, 51828, 4445, 3190, 45990], 'labels': [-1, -1, 1, -1, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][151]['training']={}
store['active_learning_steps'][151]['training']['epochs']=[]
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7143361568450928})
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5293642282485962})
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5775203704833984})
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.4981406033039093})
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5650744438171387})
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5398967266082764})
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5206459164619446})
store['active_learning_steps'][151]['training']['best_epoch']=4
store['active_learning_steps'][151]['evaluation_metrics']={'accuracy': 0.9349, 'crossentropy': 0.4413876953125}
store['active_learning_steps'][151]['acquisition']={'indices': [20841, 59321, 48154, 34933, 16865], 'labels': [9, 4, -1, -1, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][152]['training']={}
store['active_learning_steps'][152]['training']['epochs']=[]
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6526992321014404})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5486456155776978})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6142377853393555})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5353679656982422})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5763282775878906})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5967141389846802})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.5543233156204224})
store['active_learning_steps'][152]['training']['best_epoch']=4
store['active_learning_steps'][152]['evaluation_metrics']={'accuracy': 0.9383, 'crossentropy': 0.41593115234375}
store['active_learning_steps'][152]['acquisition']={'indices': [59599, 49539, 53090, 16694, 42793], 'labels': [4, -1, 8, 1, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][153]['training']={}
store['active_learning_steps'][153]['training']['epochs']=[]
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6494244337081909})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.543146550655365})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5687633752822876})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5478014945983887})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6149920225143433})
store['active_learning_steps'][153]['training']['best_epoch']=2
store['active_learning_steps'][153]['evaluation_metrics']={'accuracy': 0.9198, 'crossentropy': 0.481009228515625}
store['active_learning_steps'][153]['acquisition']={'indices': [47863, 19882, 31671, 41697, 31848], 'labels': [-1, -1, 7, 7, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][154]['training']={}
store['active_learning_steps'][154]['training']['epochs']=[]
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.6522576212882996})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5160449743270874})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.49582189321517944})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5144115686416626})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5372328758239746})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5472965240478516})
store['active_learning_steps'][154]['training']['best_epoch']=3
store['active_learning_steps'][154]['evaluation_metrics']={'accuracy': 0.9302, 'crossentropy': 0.42516259765625}
store['active_learning_steps'][154]['acquisition']={'indices': [21691, 14715, 54956, 48987, 37156], 'labels': [-1, 4, 2, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][155]['training']={}
store['active_learning_steps'][155]['training']['epochs']=[]
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.6646674871444702})
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5405093431472778})
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5377004146575928})
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5072968602180481})
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.572504997253418})
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5722560882568359})
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5816409587860107})
store['active_learning_steps'][155]['training']['best_epoch']=4
store['active_learning_steps'][155]['evaluation_metrics']={'accuracy': 0.9348, 'crossentropy': 0.4222080078125}
store['active_learning_steps'][155]['acquisition']={'indices': [39120, 1519, 59155, 19341, 3307], 'labels': [-1, 8, -1, 7, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][156]['training']={}
store['active_learning_steps'][156]['training']['epochs']=[]
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.7268621921539307})
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5158116221427917})
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5406545996665955})
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.48024988174438477})
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5347788333892822})
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.6142208576202393})
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5199291706085205})
store['active_learning_steps'][156]['training']['best_epoch']=4
store['active_learning_steps'][156]['evaluation_metrics']={'accuracy': 0.9392, 'crossentropy': 0.4091890625}
store['active_learning_steps'][156]['acquisition']={'indices': [56767, 54375, 48477, 29661, 52047], 'labels': [6, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][157]['training']={}
store['active_learning_steps'][157]['training']['epochs']=[]
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.6863858699798584})
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5191592574119568})
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5680016279220581})
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5280340313911438})
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5623693466186523})
store['active_learning_steps'][157]['training']['best_epoch']=2
store['active_learning_steps'][157]['evaluation_metrics']={'accuracy': 0.9254, 'crossentropy': 0.478827392578125}
store['active_learning_steps'][157]['acquisition']={'indices': [46364, 36281, 45805, 16541, 4125], 'labels': [-1, 7, -1, -1, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][158]['training']={}
store['active_learning_steps'][158]['training']['epochs']=[]
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5997428297996521})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5043396949768066})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5008715987205505})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5713013410568237})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5563928484916687})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5212551355361938})
store['active_learning_steps'][158]['training']['best_epoch']=3
store['active_learning_steps'][158]['evaluation_metrics']={'accuracy': 0.9299, 'crossentropy': 0.45112509765625}
store['active_learning_steps'][158]['acquisition']={'indices': [13683, 39329, 40471, 16985, 57670], 'labels': [-1, 3, -1, 4, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][159]['training']={}
store['active_learning_steps'][159]['training']['epochs']=[]
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6819339990615845})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5568609237670898})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.514419436454773})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5287309288978577})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.543511688709259})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5990175008773804})
store['active_learning_steps'][159]['training']['best_epoch']=3
store['active_learning_steps'][159]['evaluation_metrics']={'accuracy': 0.9286, 'crossentropy': 0.470874951171875}
store['active_learning_steps'][159]['acquisition']={'indices': [31930, 18672, 8079, 24365, 47197], 'labels': [-1, 6, 7, 4, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][160]['training']={}
store['active_learning_steps'][160]['training']['epochs']=[]
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.7263444066047668})
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.554985523223877})
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5263261795043945})
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6479387283325195})
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5484932661056519})
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5805802345275879})
store['active_learning_steps'][160]['training']['best_epoch']=3
store['active_learning_steps'][160]['evaluation_metrics']={'accuracy': 0.9316, 'crossentropy': 0.42812509765625}
store['active_learning_steps'][160]['acquisition']={'indices': [57927, 13012, 37275, 36541, 56835], 'labels': [-1, -1, -1, 8, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][161]['training']={}
store['active_learning_steps'][161]['training']['epochs']=[]
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6832237243652344})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6015592217445374})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4950219690799713})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5111509561538696})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.518078088760376})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4950510859489441})
store['active_learning_steps'][161]['training']['best_epoch']=3
store['active_learning_steps'][161]['evaluation_metrics']={'accuracy': 0.9314, 'crossentropy': 0.43761455078125}
store['active_learning_steps'][161]['acquisition']={'indices': [55138, 56948, 58635, 3055, 17375], 'labels': [6, -1, 7, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][162]['training']={}
store['active_learning_steps'][162]['training']['epochs']=[]
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6603373289108276})
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5151383876800537})
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5694138407707214})
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5422333478927612})
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.45631110668182373})
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5077343583106995})
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5106220245361328})
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5446853041648865})
store['active_learning_steps'][162]['training']['best_epoch']=5
store['active_learning_steps'][162]['evaluation_metrics']={'accuracy': 0.9407, 'crossentropy': 0.4021874267578125}
store['active_learning_steps'][162]['acquisition']={'indices': [48632, 58802, 19993, 58704, 12216], 'labels': [-1, 5, 6, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][163]['training']={}
store['active_learning_steps'][163]['training']['epochs']=[]
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7364363670349121})
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.529407262802124})
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5275071859359741})
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5272197723388672})
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5552043914794922})
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5744737386703491})
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5689107179641724})
store['active_learning_steps'][163]['training']['best_epoch']=4
store['active_learning_steps'][163]['evaluation_metrics']={'accuracy': 0.9324, 'crossentropy': 0.452185791015625}
store['active_learning_steps'][163]['acquisition']={'indices': [40434, 30683, 36041, 28379, 16823], 'labels': [-1, -1, 7, 7, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][164]['training']={}
store['active_learning_steps'][164]['training']['epochs']=[]
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6947937607765198})
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5293762683868408})
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.496845006942749})
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.546255886554718})
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4913616478443146})
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4898710250854492})
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5128726363182068})
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5271186232566833})
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5874425172805786})
store['active_learning_steps'][164]['training']['best_epoch']=6
store['active_learning_steps'][164]['evaluation_metrics']={'accuracy': 0.9462, 'crossentropy': 0.388986474609375}
store['active_learning_steps'][164]['acquisition']={'indices': [48939, 57506, 49914, 10051, 34012], 'labels': [5, -1, -1, 5, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][165]['training']={}
store['active_learning_steps'][165]['training']['epochs']=[]
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.6979514360427856})
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.526800274848938})
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4618470072746277})
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5211212038993835})
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5269975662231445})
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4964500665664673})
store['active_learning_steps'][165]['training']['best_epoch']=3
store['active_learning_steps'][165]['evaluation_metrics']={'accuracy': 0.9317, 'crossentropy': 0.4324970703125}
store['active_learning_steps'][165]['acquisition']={'indices': [17087, 29820, 524, 56610, 57967], 'labels': [-1, 4, -1, 1, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][166]['training']={}
store['active_learning_steps'][166]['training']['epochs']=[]
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.6626933813095093})
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.4838525056838989})
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.47799819707870483})
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.4815813899040222})
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4704235792160034})
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5012776851654053})
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.510928750038147})
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.463484525680542})
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4904262125492096})
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.561345100402832})
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5699464082717896})
store['active_learning_steps'][166]['training']['best_epoch']=8
store['active_learning_steps'][166]['evaluation_metrics']={'accuracy': 0.945, 'crossentropy': 0.405943017578125}
store['active_learning_steps'][166]['acquisition']={'indices': [20669, 23822, 42048, 18853, 33151], 'labels': [-1, -1, 9, 1, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][167]['training']={}
store['active_learning_steps'][167]['training']['epochs']=[]
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.6640950441360474})
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5091673135757446})
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5135959386825562})
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4708901047706604})
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5504715442657471})
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5232130289077759})
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5421808958053589})
store['active_learning_steps'][167]['training']['best_epoch']=4
store['active_learning_steps'][167]['evaluation_metrics']={'accuracy': 0.9382, 'crossentropy': 0.415367041015625}
store['active_learning_steps'][167]['acquisition']={'indices': [56260, 37334, 54224, 9514, 58365], 'labels': [3, -1, 6, -1, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][168]['training']={}
store['active_learning_steps'][168]['training']['epochs']=[]
store['active_learning_steps'][168]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.7581429481506348})
store['active_learning_steps'][168]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5586315989494324})
store['active_learning_steps'][168]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5352182388305664})
store['active_learning_steps'][168]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5339441895484924})
store['active_learning_steps'][168]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5750331878662109})
store['active_learning_steps'][168]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5896497964859009})
store['active_learning_steps'][168]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.6136599183082581})
store['active_learning_steps'][168]['training']['best_epoch']=4
store['active_learning_steps'][168]['evaluation_metrics']={'accuracy': 0.9369, 'crossentropy': 0.4363654296875}
store['active_learning_steps'][168]['acquisition']={'indices': [44787, 30324, 38791, 43232, 28399], 'labels': [7, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][169]['training']={}
store['active_learning_steps'][169]['training']['epochs']=[]
store['active_learning_steps'][169]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.7001124620437622})
store['active_learning_steps'][169]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5103408694267273})
store['active_learning_steps'][169]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4295518100261688})
store['active_learning_steps'][169]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5027437806129456})
store['active_learning_steps'][169]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5139907598495483})
store['active_learning_steps'][169]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5750317573547363})
store['active_learning_steps'][169]['training']['best_epoch']=3
store['active_learning_steps'][169]['evaluation_metrics']={'accuracy': 0.9391, 'crossentropy': 0.3924043212890625}
store['active_learning_steps'][169]['acquisition']={'indices': [28237, 3616, 45302, 31399, 53452], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][170]['training']={}
store['active_learning_steps'][170]['training']['epochs']=[]
store['active_learning_steps'][170]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6310294270515442})
store['active_learning_steps'][170]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5421313047409058})
store['active_learning_steps'][170]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.487440288066864})
store['active_learning_steps'][170]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5119771957397461})
store['active_learning_steps'][170]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4805683195590973})
store['active_learning_steps'][170]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5162727236747742})
store['active_learning_steps'][170]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5312470197677612})
store['active_learning_steps'][170]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.5068780183792114})
store['active_learning_steps'][170]['training']['best_epoch']=5
store['active_learning_steps'][170]['evaluation_metrics']={'accuracy': 0.9415, 'crossentropy': 0.403738916015625}
store['active_learning_steps'][170]['acquisition']={'indices': [34037, 11140, 16066, 34284, 52309], 'labels': [0, -1, 8, 6, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][171]['training']={}
store['active_learning_steps'][171]['training']['epochs']=[]
store['active_learning_steps'][171]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6119847297668457})
store['active_learning_steps'][171]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.505754828453064})
store['active_learning_steps'][171]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.4737768769264221})
store['active_learning_steps'][171]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5210666656494141})
store['active_learning_steps'][171]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5019181966781616})
store['active_learning_steps'][171]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4713905453681946})
store['active_learning_steps'][171]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5112031698226929})
store['active_learning_steps'][171]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5129944086074829})
store['active_learning_steps'][171]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.46260151267051697})
store['active_learning_steps'][171]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.548440158367157})
store['active_learning_steps'][171]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5109540224075317})
store['active_learning_steps'][171]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4581252932548523})
store['active_learning_steps'][171]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.589686930179596})
store['active_learning_steps'][171]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5105201601982117})
store['active_learning_steps'][171]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5738434791564941})
store['active_learning_steps'][171]['training']['best_epoch']=12
store['active_learning_steps'][171]['evaluation_metrics']={'accuracy': 0.9486, 'crossentropy': 0.4057505615234375}
store['active_learning_steps'][171]['acquisition']={'indices': [14631, 58365, 56463, 27792, 30140], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][172]['training']={}
store['active_learning_steps'][172]['training']['epochs']=[]
store['active_learning_steps'][172]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6101593971252441})
store['active_learning_steps'][172]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.513058066368103})
store['active_learning_steps'][172]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.443342924118042})
store['active_learning_steps'][172]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.49142348766326904})
store['active_learning_steps'][172]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.48269933462142944})
store['active_learning_steps'][172]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5017238259315491})
store['active_learning_steps'][172]['training']['best_epoch']=3
store['active_learning_steps'][172]['evaluation_metrics']={'accuracy': 0.9367, 'crossentropy': 0.40641748046875}
store['active_learning_steps'][172]['acquisition']={'indices': [38779, 58582, 32413, 21454, 17732], 'labels': [1, -1, -1, 0, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][173]['training']={}
store['active_learning_steps'][173]['training']['epochs']=[]
store['active_learning_steps'][173]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6149269342422485})
store['active_learning_steps'][173]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5157142877578735})
store['active_learning_steps'][173]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5232052206993103})
store['active_learning_steps'][173]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5252343416213989})
store['active_learning_steps'][173]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5108597278594971})
store['active_learning_steps'][173]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5161617994308472})
store['active_learning_steps'][173]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5767810344696045})
store['active_learning_steps'][173]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5723500847816467})
store['active_learning_steps'][173]['training']['best_epoch']=5
store['active_learning_steps'][173]['evaluation_metrics']={'accuracy': 0.9367, 'crossentropy': 0.42359453125}
store['active_learning_steps'][173]['acquisition']={'indices': [14770, 48221, 53042, 36091, 56247], 'labels': [7, -1, 3, -1, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][174]['training']={}
store['active_learning_steps'][174]['training']['epochs']=[]
store['active_learning_steps'][174]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.710070788860321})
store['active_learning_steps'][174]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5255733728408813})
store['active_learning_steps'][174]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.502281904220581})
store['active_learning_steps'][174]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.49810460209846497})
store['active_learning_steps'][174]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.47336041927337646})
store['active_learning_steps'][174]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5117980241775513})
store['active_learning_steps'][174]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4825717806816101})
store['active_learning_steps'][174]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.48292383551597595})
store['active_learning_steps'][174]['training']['best_epoch']=5
store['active_learning_steps'][174]['evaluation_metrics']={'accuracy': 0.9439, 'crossentropy': 0.3987528076171875}
store['active_learning_steps'][174]['acquisition']={'indices': [49834, 1446, 29060, 27424, 56769], 'labels': [-1, 4, -1, 4, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][175]['training']={}
store['active_learning_steps'][175]['training']['epochs']=[]
store['active_learning_steps'][175]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.6975851058959961})
store['active_learning_steps'][175]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5270726680755615})
store['active_learning_steps'][175]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5610349774360657})
store['active_learning_steps'][175]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5080336332321167})
store['active_learning_steps'][175]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5615215301513672})
store['active_learning_steps'][175]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.49249857664108276})
store['active_learning_steps'][175]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5229330658912659})
store['active_learning_steps'][175]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5332800149917603})
store['active_learning_steps'][175]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5517182350158691})
store['active_learning_steps'][175]['training']['best_epoch']=6
store['active_learning_steps'][175]['evaluation_metrics']={'accuracy': 0.9416, 'crossentropy': 0.42368720703125}
