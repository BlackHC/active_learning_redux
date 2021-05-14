store = {}
store['timestamp']=1620908077
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py', '--id=6']
store['commit']='7a88a46c213fc419b8e48358058ec72fe5b0f546'
store['github_url']='7a88a46c213fc419b8e48358058ec72fe5b0f546'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py'
store['job_id']=6
store['worker_id']=6
store['num_workers']=20
store['config']={'seed': 1243, 'acquisition_size': 10, 'max_training_set': 450, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'evaluation_set_size': 100, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'min_samples_per_epoch': 5056, 'mnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.TemperedEvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples)) + ('OoD Dataset (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastMNIST (test, 10000 samples)'"}
store['initial_training_set_indices']=[53434, 8533, 14640, 39579, 30392, 58125, 37915, 3091, 57520, 43803, 44119, 52296, 58226, 40334, 46037, 22015, 22304, 43812, 12640, 53689]
store['evaluation_set_indices']=[29974, 55573, 35472, 44048, 48031, 5616, 10110, 47420, 56990, 34198, 3792, 5715, 15969, 32775, 19757, 34588, 28991, 47417, 26501, 12108, 5573, 48032, 40646, 43252, 2404, 36797, 29079, 40018, 37047, 41512, 45567, 801, 10664, 52801, 42890, 32972, 45974, 20801, 23496, 5803, 10508, 46870, 49549, 306, 38725, 13074, 19689, 27135, 16068, 18137, 2728, 43321, 29950, 380, 27254, 50466, 31965, 24052, 44454, 20076, 21423, 58741, 27145, 38430, 37354, 49986, 4321, 12610, 34482, 35794, 396, 50036, 46861, 57811, 53831, 49304, 51555, 29614, 767, 23451, 49512, 26479, 50997, 1774, 44803, 55187, 30013, 33736, 49169, 46464, 31444, 52440, 33486, 2206, 15675, 54426, 9574, 54012, 28833, 44428]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 2.247647285461426})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 2.764303684234619})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.5868282318115234})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 2.9454288482666016})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6869, 'crossentropy': 2.0332689453125}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.15549635887146})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.080956220626831})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.1798160076141357})
store['active_learning_steps'][0]['eval_training']['best_epoch']=2
store['active_learning_steps'][0]['acquisition']={'indices': [51002, 44023, 58428, 59395, 31753, 48166, 15854, 14313, 33197, 29118], 'labels': [0, 0, 5, 8, 0, 7, 0, -1, 2, 8], 'scores': [0.7198308110237122, 0.7330556511878967, 0.7525269389152527, 0.9209499359130859, 0.7548570036888123, 0.6612658500671387, 0.7893602252006531, 0.6917580962181091, 0.5273314118385315, 0.5931733846664429]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.8585205078125})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 2.158344268798828})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 2.324014186859131})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 2.434542655944824})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.707, 'crossentropy': 1.771559765625}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.0472753047943115})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.0012578964233398})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.0154738426208496})
store['active_learning_steps'][1]['eval_training']['best_epoch']=2
store['active_learning_steps'][1]['acquisition']={'indices': [56916, 55685, 42225, 35161, 45181, 59566, 41885, 49149, 36703, 6402], 'labels': [6, 5, 6, 2, 8, 9, 4, 3, 6, 6], 'scores': [0.5249025821685791, 0.604578971862793, 0.6292714476585388, 0.5720304846763611, 0.7105764150619507, 0.6625139117240906, 0.6828489899635315, 0.8005343675613403, 0.5768541693687439, 0.7274897694587708]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7392578125, 'crossentropy': 1.752436637878418})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 1.7738010883331299})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.755859375, 'crossentropy': 1.982659101486206})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 1.9664840698242188})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.7214, 'crossentropy': 1.63090263671875}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.7509765625, 'crossentropy': 0.985074520111084})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 0.9659853577613831})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.7412109375, 'crossentropy': 0.9380720853805542})
store['active_learning_steps'][2]['eval_training']['best_epoch']=3
store['active_learning_steps'][2]['acquisition']={'indices': [42619, 33252, 4076, 55197, 3416, 11010, 40795, 26080, 41161, 49503], 'labels': [7, 9, -1, 4, 5, 3, 7, 7, 7, 5], 'scores': [0.468104749917984, 0.6256409585475922, 0.4074892997741699, 0.5294195115566254, 0.6028309464454651, 0.5648117065429688, 0.5607329607009888, 0.6596400141716003, 0.47251152992248535, 0.6487026810646057]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 1.1769874095916748})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 1.3991217613220215})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.5487195253372192})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 1.5833008289337158})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.7914, 'crossentropy': 1.1757521484375}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 0.8649077415466309})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 0.7700559496879578})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 0.8037357926368713})
store['active_learning_steps'][3]['eval_training']['best_epoch']=2
store['active_learning_steps'][3]['acquisition']={'indices': [44455, 12529, 24602, 11550, 41410, 45094, 40846, 37324, 36744, 49838], 'labels': [2, -1, 2, 9, 6, 2, 4, 8, 1, 6], 'scores': [0.48764607310295105, 0.34960615634918213, 0.6426315903663635, 0.5418263673782349, 0.5433452129364014, 0.6823829412460327, 0.6422160267829895, 0.555982232093811, 0.4904775023460388, 0.5726835131645203]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.006331205368042})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 1.3024592399597168})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.2311885356903076})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 1.316009283065796})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.814, 'crossentropy': 0.9504685546875}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 0.8421701192855835})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 0.7382099628448486})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 0.7276826500892639})
store['active_learning_steps'][4]['eval_training']['best_epoch']=3
store['active_learning_steps'][4]['acquisition']={'indices': [26260, 32106, 38577, 58024, 40621, 35329, 44236, 32080, 19423, 27274], 'labels': [-1, 3, 5, 8, -1, 1, 9, 5, 2, 3], 'scores': [0.3007810115814209, 0.538590669631958, 0.47198379039764404, 0.37326139211654663, 0.3473021984100342, 0.41564905643463135, 0.4919799566268921, 0.666816234588623, 0.4771236777305603, 0.4713597297668457]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 1.0397379398345947})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 1.0305144786834717})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 1.019287347793579})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 1.2067477703094482})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 1.1672773361206055})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 1.1722958087921143})
store['active_learning_steps'][5]['training']['best_epoch']=3
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.8531, 'crossentropy': 1.01744736328125}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 0.8113254308700562})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.6401680111885071})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.6211042404174805})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.5879665613174438})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.5604188442230225})
store['active_learning_steps'][5]['eval_training']['best_epoch']=5
store['active_learning_steps'][5]['acquisition']={'indices': [8940, 12873, 34829, 17379, 48587, 22603, 26260, 40553, 19244, 15855], 'labels': [6, 4, 5, 0, 3, 0, -1, 8, 9, 5], 'scores': [0.5195263028144836, 0.4487968683242798, 0.7131444215774536, 0.4071018695831299, 0.5728154182434082, 0.5946514010429382, 0.5226174592971802, 0.59438157081604, 0.667465329170227, 0.7049621939659119]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 0.9688222408294678})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.9843329191207886})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 1.0785974264144897})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 1.0852127075195312})
store['active_learning_steps'][6]['training']['best_epoch']=1
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.8319, 'crossentropy': 0.88722529296875}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.8899205923080444})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 0.8050500154495239})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.7380479574203491})
store['active_learning_steps'][6]['eval_training']['best_epoch']=3
store['active_learning_steps'][6]['acquisition']={'indices': [26628, 4290, 4938, 58660, 32606, 24632, 54902, 10800, 20048, 1317], 'labels': [8, 5, 2, 3, 2, 2, 5, 8, 7, 3], 'scores': [0.3920900821685791, 0.5776881575584412, 0.431693434715271, 0.45364630222320557, 0.39601635932922363, 0.3728727102279663, 0.4505958557128906, 0.43492603302001953, 0.32289087772369385, 0.5208563804626465]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 0.8966218829154968})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.8487502336502075})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.8714005947113037})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.91225266456604})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 1.0842844247817993})
store['active_learning_steps'][7]['training']['best_epoch']=2
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.8719, 'crossentropy': 0.83174033203125}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 0.7614649534225464})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.6057717800140381})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.5343902111053467})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.5689396858215332})
store['active_learning_steps'][7]['eval_training']['best_epoch']=3
store['active_learning_steps'][7]['acquisition']={'indices': [29501, 50410, 29508, 20372, 43146, 23076, 16488, 11853, 24134, 30776], 'labels': [2, 8, 7, 8, 9, 3, 9, 9, 8, 9], 'scores': [0.6038493514060974, 0.5341857671737671, 0.4712412357330322, 0.46469342708587646, 0.6220185160636902, 0.46358388662338257, 0.37688347697257996, 0.6501704454421997, 0.5430229902267456, 0.36967623233795166]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.8704400062561035})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.842458963394165})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.850150465965271})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.8403710722923279})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.8775792717933655})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.9350822567939758})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.9527343511581421})
store['active_learning_steps'][8]['training']['best_epoch']=4
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.8946, 'crossentropy': 0.726298779296875}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.8226822018623352})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5586300492286682})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5240355730056763})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.5019849538803101})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.4652775824069977})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.48864495754241943})
store['active_learning_steps'][8]['eval_training']['best_epoch']=5
store['active_learning_steps'][8]['acquisition']={'indices': [16590, 35061, 53538, 18962, 11711, 35401, 31717, 38136, 9583, 38566], 'labels': [6, 8, 5, 7, 2, 3, 4, 8, 2, -1], 'scores': [0.6006442308425903, 0.37340909242630005, 0.5397895574569702, 0.447648823261261, 0.5744130611419678, 0.40614718198776245, 0.5352325439453125, 0.49599021673202515, 0.3855789005756378, 0.3130166530609131]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 0.8822907209396362})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.7664364576339722})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7863807082176208})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.8632562160491943})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.7999591827392578})
store['active_learning_steps'][9]['training']['best_epoch']=2
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.8923, 'crossentropy': 0.668496826171875}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.7346178293228149})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5844671726226807})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5707981586456299})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.5479745864868164})
store['active_learning_steps'][9]['eval_training']['best_epoch']=4
store['active_learning_steps'][9]['acquisition']={'indices': [14733, 1003, 49205, 11789, 14825, 37397, 25546, 33417, 14581, 24719], 'labels': [8, 1, 1, 7, 3, 3, 8, 1, 7, 4], 'scores': [0.4807676672935486, 0.48128002882003784, 0.4398213028907776, 0.6577416062355042, 0.583778440952301, 0.5516641736030579, 0.5049027800559998, 0.47202545404434204, 0.5496205687522888, 0.4323962330818176]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.8738530874252319})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.710930585861206})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6520037651062012})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.8001724481582642})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.7371455430984497})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.8444135189056396})
store['active_learning_steps'][10]['training']['best_epoch']=3
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.9059, 'crossentropy': 0.608714208984375}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7112522125244141})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5195935964584351})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.4911753237247467})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.45301738381385803})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.44662389159202576})
store['active_learning_steps'][10]['eval_training']['best_epoch']=5
store['active_learning_steps'][10]['acquisition']={'indices': [21355, 47513, 108, 41054, 29061, 1352, 53330, 14878, 53880, 14749], 'labels': [0, 0, 0, 7, 3, 9, 1, 3, 0, 0], 'scores': [0.6218670606613159, 0.5101668834686279, 0.5108836591243744, 0.7314504384994507, 0.530876636505127, 0.5207682847976685, 0.5069095492362976, 0.5990782380104065, 0.6111043989658356, 0.7220656871795654]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.8298117518424988})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6350575685501099})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7335257530212402})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7024388313293457})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6871668100357056})
store['active_learning_steps'][11]['training']['best_epoch']=2
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.8966, 'crossentropy': 0.60664775390625}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.7705869674682617})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.5790504217147827})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.48979151248931885})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.506809413433075})
store['active_learning_steps'][11]['eval_training']['best_epoch']=3
store['active_learning_steps'][11]['acquisition']={'indices': [11492, 31046, 34718, 17290, 30792, 36450, 14760, 37794, 7168, 37183], 'labels': [5, 6, 2, -1, 4, 2, 2, 4, 8, -1], 'scores': [0.18745112419128418, 0.6179282069206238, 0.4764593243598938, 0.24223709106445312, 0.4513588547706604, 0.6566395163536072, 0.4568063020706177, 0.6111109256744385, 0.6241166591644287, 0.3633235692977905]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.8182797431945801})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7064303755760193})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7055130004882812})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.7474716901779175})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.7186506986618042})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.8025038838386536})
store['active_learning_steps'][12]['training']['best_epoch']=3
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.9102, 'crossentropy': 0.593252978515625}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.8002160787582397})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5493849515914917})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.48130035400390625})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.4743690490722656})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.44725602865219116})
store['active_learning_steps'][12]['eval_training']['best_epoch']=5
store['active_learning_steps'][12]['acquisition']={'indices': [45462, 17903, 53185, 48638, 54099, 16817, 19747, 50149, 26982, 28618], 'labels': [2, 9, -1, 0, 7, 0, 9, 4, -1, 9], 'scores': [0.5649682581424713, 0.6447039842605591, 0.432811975479126, 0.5726717114448547, 0.5319027900695801, 0.4254394769668579, 0.4302266240119934, 0.5398478507995605, 0.31920671463012695, 0.5414210557937622]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.8792060613632202})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6521376967430115})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.658854603767395})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6741753816604614})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6971848011016846})
store['active_learning_steps'][13]['training']['best_epoch']=2
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.9078, 'crossentropy': 0.56124443359375}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.7550109624862671})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5461161136627197})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.48797500133514404})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.4785219132900238})
store['active_learning_steps'][13]['eval_training']['best_epoch']=4
store['active_learning_steps'][13]['acquisition']={'indices': [41568, 11373, 40959, 45024, 33420, 56244, 41020, 49624, 29570, 33956], 'labels': [4, 9, 5, 5, 5, 4, 4, 6, 0, 8], 'scores': [0.3645714521408081, 0.3796011209487915, 0.5044841170310974, 0.4969797134399414, 0.4494630694389343, 0.5007484555244446, 0.3491153120994568, 0.5545819401741028, 0.46639901399612427, 0.4947888255119324]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.8706326484680176})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6110994219779968})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.595854640007019})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5727107524871826})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6372332572937012})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6503067016601562})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6075888872146606})
store['active_learning_steps'][14]['training']['best_epoch']=4
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.9274, 'crossentropy': 0.503231591796875}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.778244137763977})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.524728536605835})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.4877117872238159})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.4312123656272888})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.4269397556781769})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.40222692489624023})
store['active_learning_steps'][14]['eval_training']['best_epoch']=6
store['active_learning_steps'][14]['acquisition']={'indices': [28136, 54377, 47056, 36078, 34678, 41962, 12353, 19253, 27026, 11580], 'labels': [8, 3, 9, 3, 8, 9, -1, 8, 2, 9], 'scores': [0.6286125183105469, 0.5323095917701721, 0.6518726348876953, 0.5060575604438782, 0.6855030655860901, 0.5998261868953705, 0.4163169860839844, 0.5479632019996643, 0.49778056144714355, 0.5444239377975464]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.8623042106628418})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.574343204498291})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5272183418273926})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5365979075431824})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.576601505279541})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6028977632522583})
store['active_learning_steps'][15]['training']['best_epoch']=3
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.9264, 'crossentropy': 0.484819287109375}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.7287328243255615})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.4980134665966034})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4369213581085205})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.39526623487472534})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.4357225000858307})
store['active_learning_steps'][15]['eval_training']['best_epoch']=4
store['active_learning_steps'][15]['acquisition']={'indices': [36704, 30177, 42004, 15406, 31339, 38158, 54521, 9656, 20292, 54951], 'labels': [2, 7, 7, 8, 6, 8, 4, 7, 0, 2], 'scores': [0.43848860263824463, 0.40164637565612793, 0.2971012592315674, 0.40317070484161377, 0.3992788791656494, 0.3758249878883362, 0.3718045949935913, 0.27833181619644165, 0.34299802780151367, 0.4526616334915161]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.8290152549743652})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5074292421340942})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5013473033905029})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.44288212060928345})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.48119011521339417})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5184328556060791})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5185715556144714})
store['active_learning_steps'][16]['training']['best_epoch']=4
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.9439, 'crossentropy': 0.42875517578125}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7508962154388428})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.47608280181884766})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4218932092189789})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.3880782127380371})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.3529871106147766})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.3348594605922699})
store['active_learning_steps'][16]['eval_training']['best_epoch']=6
store['active_learning_steps'][16]['acquisition']={'indices': [18426, 28530, 49354, 49352, 35971, 2232, 12602, 47769, 29065, 29534], 'labels': [3, 9, 0, 5, 0, 3, 3, 5, -1, 5], 'scores': [0.5586581826210022, 0.313992977142334, 0.5970175862312317, 0.5874548554420471, 0.6299996376037598, 0.6114243865013123, 0.3005756139755249, 0.2736501097679138, 0.42003560066223145, 0.5434431433677673]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.8884139060974121})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5595617294311523})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.48139655590057373})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.45767056941986084})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5175368189811707})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5267635583877563})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.49782150983810425})
store['active_learning_steps'][17]['training']['best_epoch']=4
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.941, 'crossentropy': 0.403769189453125}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6824854612350464})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5059947967529297})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4356567859649658})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.3591803312301636})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.3633371591567993})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.34460586309432983})
store['active_learning_steps'][17]['eval_training']['best_epoch']=6
store['active_learning_steps'][17]['acquisition']={'indices': [18348, 54889, 54498, 15738, 34052, 32473, 485, 17552, 40595, 2928], 'labels': [8, 8, 8, -1, 9, 8, 8, -1, 8, 5], 'scores': [0.4204680323600769, 0.4208151698112488, 0.23730725049972534, 0.5339043736457825, 0.4938920736312866, 0.43973660469055176, 0.4121338129043579, 0.4125148057937622, 0.7549635767936707, 0.38803601264953613]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.8386611938476562})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5315537452697754})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.443562775850296})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.4248608946800232})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4888942241668701})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4585939645767212})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4460901618003845})
store['active_learning_steps'][18]['training']['best_epoch']=4
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.9467, 'crossentropy': 0.4179150390625}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.8714231252670288})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5047249794006348})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4057343602180481})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.37123239040374756})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3710360527038574})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.35683149099349976})
store['active_learning_steps'][18]['eval_training']['best_epoch']=6
store['active_learning_steps'][18]['acquisition']={'indices': [26444, 26151, 57383, 49910, 5065, 48191, 26097, 19369, 18346, 9771], 'labels': [1, -1, -1, 6, 2, -1, -1, -1, 7, -1], 'scores': [0.6561990976333618, 0.4475192427635193, 0.4181941747665405, 0.5367471575737, 0.4903033375740051, 0.41546738147735596, 0.47786277532577515, 0.41424560546875, 0.43288660049438477, 0.4134160280227661]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.9266570806503296})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.585472047328949})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5009673833847046})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4441507160663605})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.48537397384643555})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4587777256965637})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4664205014705658})
store['active_learning_steps'][19]['training']['best_epoch']=4
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.9465, 'crossentropy': 0.427995263671875}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7491991519927979})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.4795648455619812})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.41475600004196167})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.386567622423172})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.35606878995895386})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3731563687324524})
store['active_learning_steps'][19]['eval_training']['best_epoch']=5
store['active_learning_steps'][19]['acquisition']={'indices': [29352, 9180, 57221, 48617, 44061, 5460, 26182, 52688, 12823, 13709], 'labels': [3, 3, -1, -1, -1, -1, -1, 6, -1, 6], 'scores': [0.45940136909484863, 0.6248427629470825, 0.524498462677002, 0.47369682788848877, 0.29666948318481445, 0.2614436149597168, 0.23518133163452148, 0.6523017287254333, 0.23492717742919922, 0.34598636627197266]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.8581825494766235})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5873185396194458})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5079185962677002})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4958401918411255})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4967438578605652})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4756927788257599})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5289512872695923})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5821505784988403})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5312202572822571})
store['active_learning_steps'][20]['training']['best_epoch']=6
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.9352, 'crossentropy': 0.45785751953125}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7963619232177734})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5260772705078125})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.441942036151886})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.40030914545059204})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.36055612564086914})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.3826531767845154})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.3396340012550354})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.32981687784194946})
store['active_learning_steps'][20]['eval_training']['best_epoch']=8
store['active_learning_steps'][20]['acquisition']={'indices': [54960, 15333, 10777, 17556, 3694, 5720, 45490, 25836, 10481, 12898], 'labels': [4, -1, -1, -1, -1, 4, 5, -1, 6, -1], 'scores': [0.5781089663505554, 0.5045086145401001, 0.5196890830993652, 0.47081685066223145, 0.5522067546844482, 0.5359867215156555, 0.31639835238456726, 0.38447821140289307, 0.4531317949295044, 0.2902980446815491]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.8895421028137207})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5272183418273926})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.47054097056388855})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.47488874197006226})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.45730525255203247})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.5053635239601135})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.5101145505905151})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.5175396800041199})
store['active_learning_steps'][21]['training']['best_epoch']=5
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.9431, 'crossentropy': 0.4196787109375}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6412847638130188})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4486388862133026})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3758395314216614})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3281659185886383})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.34464535117149353})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.334165096282959})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.28378570079803467})
store['active_learning_steps'][21]['eval_training']['best_epoch']=7
store['active_learning_steps'][21]['acquisition']={'indices': [2895, 56006, 46163, 23086, 53906, 59919, 35983, 48102, 52975, 53638], 'labels': [-1, 3, 2, 8, 8, 1, -1, 7, 2, 5], 'scores': [0.4353516697883606, 0.49616140127182007, 0.6098758578300476, 0.5514450669288635, 0.5932676792144775, 0.4910936951637268, 0.39773809909820557, 0.4558316469192505, 0.45386022329330444, 0.36681991815567017]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 1.0290279388427734})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6146103143692017})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.47113463282585144})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4920937120914459})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4990174472332001})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5295529365539551})
store['active_learning_steps'][22]['training']['best_epoch']=3
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.939, 'crossentropy': 0.436315966796875}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.8214017152786255})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.502206563949585})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4615638256072998})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4050482511520386})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4129924476146698})
store['active_learning_steps'][22]['eval_training']['best_epoch']=4
store['active_learning_steps'][22]['acquisition']={'indices': [42687, 45325, 38378, 20169, 7924, 32537, 52294, 5434, 12898, 46903], 'labels': [5, 4, 5, 4, 8, 5, 0, -1, 5, -1], 'scores': [0.6016252636909485, 0.2972090542316437, 0.28741204738616943, 0.3785243630409241, 0.4346059560775757, 0.4608554244041443, 0.5394876599311829, 0.2966461181640625, 0.49124258756637573, 0.27917397022247314]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.8328397870063782})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5388551950454712})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.4781482219696045})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4511319100856781})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4150385856628418})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.49737441539764404})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.47221142053604126})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4374748766422272})
store['active_learning_steps'][23]['training']['best_epoch']=5
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.9481, 'crossentropy': 0.395540380859375}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.7374987602233887})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.473128080368042})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3791400194168091})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.36384496092796326})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3464466631412506})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.35108327865600586})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.31782829761505127})
store['active_learning_steps'][23]['eval_training']['best_epoch']=7
store['active_learning_steps'][23]['acquisition']={'indices': [7624, 28366, 37281, 30872, 36544, 24189, 53195, 29788, 56336, 39417], 'labels': [2, 2, -1, 2, -1, -1, -1, 4, -1, -1], 'scores': [0.5437861680984497, 0.5032376050949097, 0.45025956630706787, 0.3666016459465027, 0.40563905239105225, 0.4046347141265869, 0.39270174503326416, 0.5598596334457397, 0.4235173463821411, 0.28604865074157715]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.975354790687561})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.519384503364563})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.45081859827041626})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4825083613395691})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4412970542907715})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4548589587211609})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.49520108103752136})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.43290793895721436})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.46999263763427734})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4649428725242615})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.47766217589378357})
store['active_learning_steps'][24]['training']['best_epoch']=8
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.9495, 'crossentropy': 0.411967138671875}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.7155841588973999})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.44652682542800903})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3658834397792816})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.37127041816711426})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.33658522367477417})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3088511824607849})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.326640248298645})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.2955109477043152})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3325665295124054})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.2963084578514099})
store['active_learning_steps'][24]['eval_training']['best_epoch']=8
store['active_learning_steps'][24]['acquisition']={'indices': [17542, 54771, 4845, 52123, 10251, 17203, 9130, 40260, 47732, 59188], 'labels': [-1, -1, 5, 9, -1, 4, 1, -1, 4, -1], 'scores': [0.5414625406265259, 0.3861103057861328, 0.54658642411232, 0.549553632736206, 0.5387067794799805, 0.4798765182495117, 0.3972352147102356, 0.4294198155403137, 0.6486532688140869, 0.44279390573501587]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 1.0159451961517334})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4980841875076294})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3955501914024353})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3657867908477783})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4108143150806427})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.41903966665267944})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.4141114354133606})
store['active_learning_steps'][25]['training']['best_epoch']=4
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.9497, 'crossentropy': 0.3776510986328125}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.8302268981933594})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.42131513357162476})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3815506100654602})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3678399324417114})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.34974777698516846})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3528892993927002})
store['active_learning_steps'][25]['eval_training']['best_epoch']=5
store['active_learning_steps'][25]['acquisition']={'indices': [58001, 17944, 43762, 55244, 50839, 58658, 15801, 52074, 44849, 57827], 'labels': [-1, -1, 3, 7, -1, -1, 7, 4, 7, -1], 'scores': [0.3660097122192383, 0.3823198080062866, 0.315851092338562, 0.6177831292152405, 0.32128381729125977, 0.2707178592681885, 0.47585630416870117, 0.5144479870796204, 0.3903241753578186, 0.42275118827819824]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7728433012962341})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.40269070863723755})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3671715557575226})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.37512916326522827})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.36991623044013977})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4161495566368103})
store['active_learning_steps'][26]['training']['best_epoch']=3
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.9493, 'crossentropy': 0.37522255859375}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7262071371078491})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5087277889251709})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4115787148475647})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3788946270942688})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.38404425978660583})
store['active_learning_steps'][26]['eval_training']['best_epoch']=4
store['active_learning_steps'][26]['acquisition']={'indices': [47548, 38991, 18202, 54570, 16816, 602, 20172, 2764, 31293, 48173], 'labels': [8, -1, 4, 6, 9, 8, 4, -1, 8, -1], 'scores': [0.47919583320617676, 0.38732337951660156, 0.5605155229568481, 0.41056007146835327, 0.47728151082992554, 0.37423038482666016, 0.412977933883667, 0.3326129913330078, 0.4405151605606079, 0.24071061611175537]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.8920336961746216})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.46261388063430786})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.36860036849975586})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3669325113296509})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.36922118067741394})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.38922181725502014})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3572244644165039})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.39703288674354553})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3690202236175537})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.38061249256134033})
store['active_learning_steps'][27]['training']['best_epoch']=7
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.9588, 'crossentropy': 0.3614705078125}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.7525697946548462})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.42962247133255005})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3299981355667114})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.33343666791915894})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.27404850721359253})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3267298936843872})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.29472678899765015})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.284628689289093})
store['active_learning_steps'][27]['eval_training']['best_epoch']=5
store['active_learning_steps'][27]['acquisition']={'indices': [23570, 23865, 8489, 59286, 14479, 52013, 34032, 28353, 28527, 31345], 'labels': [7, 8, 0, 8, 9, -1, -1, 6, -1, 3], 'scores': [0.5085690021514893, 0.5111891627311707, 0.4699077010154724, 0.3926900029182434, 0.6340130269527435, 0.3133164644241333, 0.5641999244689941, 0.4722402095794678, 0.3735482692718506, 0.6318089365959167]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.9518067836761475})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4912530481815338})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.42461830377578735})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.39205291867256165})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.37433189153671265})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3827350437641144})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3995667099952698})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3884483575820923})
store['active_learning_steps'][28]['training']['best_epoch']=5
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.954, 'crossentropy': 0.36685703125}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.81428462266922})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.43669551610946655})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.33457404375076294})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3466905355453491})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.31233611702919006})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3229169249534607})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.32442134618759155})
store['active_learning_steps'][28]['eval_training']['best_epoch']=5
store['active_learning_steps'][28]['acquisition']={'indices': [1887, 7434, 12375, 32417, 56797, 54909, 40066, 56454, 42233, 13942], 'labels': [-1, 6, 1, 9, -1, 8, 4, 0, 4, 4], 'scores': [0.3635951280593872, 0.4495149254798889, 0.33245301246643066, 0.44054079055786133, 0.39263200759887695, 0.47486937046051025, 0.5700928568840027, 0.5378164052963257, 0.5289465188980103, 0.333834171295166]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 1.0895042419433594})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5457884669303894})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4648445248603821})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.37158727645874023})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.42786309123039246})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.39949721097946167})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.4021631181240082})
store['active_learning_steps'][29]['training']['best_epoch']=4
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.9558, 'crossentropy': 0.3657586181640625}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.7559465169906616})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5609323978424072})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.4095348119735718})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.34317171573638916})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.35302919149398804})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3312941789627075})
store['active_learning_steps'][29]['eval_training']['best_epoch']=6
store['active_learning_steps'][29]['acquisition']={'indices': [49487, 42854, 41781, 23028, 47594, 17491, 34495, 8045, 22639, 18226], 'labels': [8, 4, -1, 2, 3, 3, 2, 8, 1, -1], 'scores': [0.5034984350204468, 0.309175968170166, 0.37618911266326904, 0.5463677644729614, 0.2680637836456299, 0.3389200270175934, 0.36953505873680115, 0.5052698850631714, 0.2970980405807495, 0.37555956840515137]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.9670830368995667})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5092564821243286})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3522654175758362})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3752910792827606})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3394007086753845})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3704453110694885})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.31891006231307983})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3849092125892639})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.41313642263412476})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3763435482978821})
store['active_learning_steps'][30]['training']['best_epoch']=7
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.9596, 'crossentropy': 0.3503219970703125}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.8018503189086914})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.4888801872730255})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3777860999107361})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.33259743452072144})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.338303804397583})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.329426109790802})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.31625574827194214})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.2944411635398865})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3077428936958313})
store['active_learning_steps'][30]['eval_training']['best_epoch']=8
store['active_learning_steps'][30]['acquisition']={'indices': [25198, 20836, 56381, 54236, 57183, 30197, 13113, 44661, 30553, 31556], 'labels': [-1, -1, -1, 1, -1, -1, -1, 1, -1, 1], 'scores': [0.3992060422897339, 0.5014400482177734, 0.47380733489990234, 0.5925368666648865, 0.249619722366333, 0.35114872455596924, 0.5024564266204834, 0.5687056183815002, 0.38235151767730713, 0.6312677264213562]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.9225344657897949})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.47158461809158325})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3593333959579468})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.33917760848999023})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.34509149193763733})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3400021195411682})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3517179489135742})
store['active_learning_steps'][31]['training']['best_epoch']=4
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.9611, 'crossentropy': 0.3188888671875}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.866968035697937})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.48369383811950684})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.3952341675758362})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.35729843378067017})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.33251529932022095})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.33196693658828735})
store['active_learning_steps'][31]['eval_training']['best_epoch']=6
store['active_learning_steps'][31]['acquisition']={'indices': [42908, 33953, 18514, 7192, 50789, 38165, 44161, 50623, 13241, 22824], 'labels': [-1, -1, 2, 3, 1, 5, -1, -1, -1, -1], 'scores': [0.3483535051345825, 0.5453110933303833, 0.47248566150665283, 0.4430617690086365, 0.5163930058479309, 0.5369147658348083, 0.38039088249206543, 0.25400853157043457, 0.3376176357269287, 0.2613869905471802]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.8336395025253296})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.45819127559661865})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3598670959472656})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3278348445892334})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3556053042411804})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.34836041927337646})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3762180507183075})
store['active_learning_steps'][32]['training']['best_epoch']=4
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.9586, 'crossentropy': 0.3113511962890625}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.7192314863204956})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.49507343769073486})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.37413620948791504})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.38545018434524536})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3562440872192383})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3520221412181854})
store['active_learning_steps'][32]['eval_training']['best_epoch']=6
store['active_learning_steps'][32]['acquisition']={'indices': [25330, 51764, 30513, 19546, 20023, 33340, 38576, 51165, 228, 37500], 'labels': [5, 5, -1, 9, 3, 5, -1, -1, 3, -1], 'scores': [0.33776789903640747, 0.44111448526382446, 0.33115577697753906, 0.31851840019226074, 0.24832236766815186, 0.42385828495025635, 0.28404372930526733, 0.33987629413604736, 0.47109341621398926, 0.4344632625579834]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 1.01461923122406})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.5094523429870605})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.35751649737358093})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.37819212675094604})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.32813751697540283})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3513804078102112})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.36829495429992676})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3939658999443054})
store['active_learning_steps'][33]['training']['best_epoch']=5
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.9634, 'crossentropy': 0.3043511962890625}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.765816867351532})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4633939564228058})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3742312788963318})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.33391016721725464})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.31017500162124634})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.29386308789253235})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.29449331760406494})
store['active_learning_steps'][33]['eval_training']['best_epoch']=6
store['active_learning_steps'][33]['acquisition']={'indices': [39978, 7418, 32413, 17199, 32747, 47076, 49877, 53570, 57665, 26358], 'labels': [5, -1, 1, -1, 8, 8, 7, -1, 8, 3], 'scores': [0.2833932638168335, 0.35945022106170654, 0.5134437084197998, 0.3563615083694458, 0.5684598684310913, 0.5515408515930176, 0.23980960249900818, 0.446691632270813, 0.48164796829223633, 0.7751045227050781]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7806286215782166})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4609566330909729})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.35237184166908264})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3004753589630127})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3175416588783264})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.33211463689804077})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.30566585063934326})
store['active_learning_steps'][34]['training']['best_epoch']=4
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.9601, 'crossentropy': 0.3081729736328125}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.8727405071258545})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.49335700273513794})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.4174937605857849})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.33671391010284424})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3481144905090332})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3084263205528259})
store['active_learning_steps'][34]['eval_training']['best_epoch']=6
store['active_learning_steps'][34]['acquisition']={'indices': [4349, 25945, 44261, 47499, 44753, 11084, 24688, 7829, 55552, 13093], 'labels': [6, 1, 9, 2, 5, -1, 1, -1, -1, 3], 'scores': [0.3980432152748108, 0.35955458879470825, 0.35439902544021606, 0.2969388961791992, 0.4660329818725586, 0.24995672702789307, 0.3695247173309326, 0.4723968505859375, 0.2616499662399292, 0.3257327079772949]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.9028832316398621})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4774502217769623})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.36883676052093506})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3281009793281555})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.33041560649871826})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.33658891916275024})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.35517850518226624})
store['active_learning_steps'][35]['training']['best_epoch']=4
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.9639, 'crossentropy': 0.3049677734375}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.7929644584655762})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4592340588569641})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.370828777551651})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3252696990966797})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.30261626839637756})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3307386636734009})
store['active_learning_steps'][35]['eval_training']['best_epoch']=5
store['active_learning_steps'][35]['acquisition']={'indices': [26302, 57124, 45510, 50308, 884, 9921, 8994, 1512, 54794, 587], 'labels': [9, 5, -1, 3, 7, -1, 6, 0, 2, -1], 'scores': [0.31500333547592163, 0.4393829107284546, 0.5035678148269653, 0.2931554913520813, 0.3027840256690979, 0.3348625898361206, 0.34120118618011475, 0.44971752166748047, 0.40380167961120605, 0.2758268117904663]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.9734169840812683})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.5558840036392212})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3786084055900574})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.38070693612098694})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3280995190143585})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.36862713098526})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3619753122329712})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3775288462638855})
store['active_learning_steps'][36]['training']['best_epoch']=5
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.9619, 'crossentropy': 0.2972362060546875}
store['active_learning_steps'][36]['eval_training']={}
store['active_learning_steps'][36]['eval_training']['epochs']=[]
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7386391162872314})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4823865592479706})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4191526472568512})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.35389089584350586})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3291035294532776})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3255702257156372})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2883695363998413})
store['active_learning_steps'][36]['eval_training']['best_epoch']=7
store['active_learning_steps'][36]['acquisition']={'indices': [8918, 38144, 4017, 6924, 13954, 11044, 15664, 57041, 48158, 36008], 'labels': [8, 7, 5, 8, 8, 4, 8, 0, 2, 8], 'scores': [0.44963157176971436, 0.5228089094161987, 0.3687804937362671, 0.47768229246139526, 0.32669615745544434, 0.4867668151855469, 0.33825790882110596, 0.47336041927337646, 0.528748095035553, 0.5744237899780273]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.9383395910263062})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4853631556034088})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.43787485361099243})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3492487668991089})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.32093337178230286})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.33429577946662903})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3283393085002899})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3352031111717224})
store['active_learning_steps'][37]['training']['best_epoch']=5
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.9634, 'crossentropy': 0.300640478515625}
store['active_learning_steps'][37]['eval_training']={}
store['active_learning_steps'][37]['eval_training']['epochs']=[]
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.8335716128349304})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5396029949188232})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.39199310541152954})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.34685224294662476})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3105945885181427})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3140162229537964})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2948053479194641})
store['active_learning_steps'][37]['eval_training']['best_epoch']=7
store['active_learning_steps'][37]['acquisition']={'indices': [37281, 34706, 47936, 44520, 2323, 43045, 47870, 14539, 5109, 31369], 'labels': [-1, -1, 8, -1, -1, -1, 9, -1, 5, -1], 'scores': [0.5362503528594971, 0.38840627670288086, 0.48355430364608765, 0.3726416826248169, 0.4273890256881714, 0.4901924729347229, 0.5506683588027954, 0.4142690896987915, 0.3825206160545349, 0.32392561435699463]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.9669895172119141})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.47706395387649536})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.40337973833084106})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3251509666442871})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3229624927043915})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3272278308868408})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3219684958457947})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3351530134677887})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.37313830852508545})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.33905157446861267})
store['active_learning_steps'][38]['training']['best_epoch']=7
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.9621, 'crossentropy': 0.3044134033203125}
store['active_learning_steps'][38]['eval_training']={}
store['active_learning_steps'][38]['eval_training']['epochs']=[]
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.8192046284675598})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.44457852840423584})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3622068464756012})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.31319576501846313})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.30203527212142944})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.2951304316520691})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.28909265995025635})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.27646633982658386})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.25971174240112305})
store['active_learning_steps'][38]['eval_training']['best_epoch']=9
store['active_learning_steps'][38]['acquisition']={'indices': [50897, 39516, 38194, 11864, 10202, 57810, 18110, 2698, 43164, 12593], 'labels': [2, 5, 5, 5, 7, 0, 2, 5, -1, 3], 'scores': [0.5488932728767395, 0.5045408606529236, 0.6128093004226685, 0.5471614599227905, 0.484605610370636, 0.49839484691619873, 0.47613635659217834, 0.3491126298904419, 0.34578824043273926, 0.48201507329940796]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.8999483585357666})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.5273705124855042})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3781166076660156})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.32505863904953003})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.39876610040664673})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2960715889930725})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.33964067697525024})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.29626747965812683})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.31759577989578247})
store['active_learning_steps'][39]['training']['best_epoch']=6
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.9652, 'crossentropy': 0.2825022216796875}
store['active_learning_steps'][39]['eval_training']={}
store['active_learning_steps'][39]['eval_training']['epochs']=[]
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.8192145824432373})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.45453739166259766})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3908400535583496})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3206685185432434})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.32057803869247437})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2811909019947052})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.30602559447288513})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.2846420109272003})
store['active_learning_steps'][39]['eval_training']['best_epoch']=6
store['active_learning_steps'][39]['acquisition']={'indices': [19133, 2887, 12851, 3282, 34034, 2947, 43483, 53387, 39531, 27638], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.4725228548049927, 0.3519108295440674, 0.4753625988960266, 0.3117654323577881, 0.553107500076294, 0.2966960668563843, 0.5511499643325806, 0.30571186542510986, 0.4474831819534302, 0.3430551290512085]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 1.0022685527801514})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5342759490013123})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3916851580142975})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3251519799232483})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3766011595726013})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3418281078338623})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.34128129482269287})
store['active_learning_steps'][40]['training']['best_epoch']=4
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.9582, 'crossentropy': 0.3228953857421875}
store['active_learning_steps'][40]['eval_training']={}
store['active_learning_steps'][40]['eval_training']['epochs']=[]
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.8052387237548828})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.47364774346351624})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3899581730365753})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.34361398220062256})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.35102173686027527})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.32815873622894287})
store['active_learning_steps'][40]['eval_training']['best_epoch']=6
store['active_learning_steps'][40]['acquisition']={'indices': [33360, 40654, 45501, 32124, 57539, 15427, 59508, 41160, 54756, 24424], 'labels': [9, 5, 2, -1, -1, -1, -1, -1, 2, 1], 'scores': [0.3286573886871338, 0.5468823909759521, 0.27118784189224243, 0.3023355007171631, 0.22828972339630127, 0.35696256160736084, 0.39664924144744873, 0.3357006311416626, 0.47048306465148926, 0.7029660940170288]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.9188781976699829})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4358617663383484})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3995552957057953})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3585280179977417})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.35755008459091187})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.37137359380722046})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3428923785686493})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3593738079071045})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.37392330169677734})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.39496907591819763})
store['active_learning_steps'][41]['training']['best_epoch']=7
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.9611, 'crossentropy': 0.323255712890625}
store['active_learning_steps'][41]['eval_training']={}
store['active_learning_steps'][41]['eval_training']['epochs']=[]
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.863344669342041})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.497989296913147})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3639102578163147})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.33297204971313477})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.27599525451660156})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.27704715728759766})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2966545522212982})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2961995303630829})
store['active_learning_steps'][41]['eval_training']['best_epoch']=5
store['active_learning_steps'][41]['acquisition']={'indices': [23260, 26824, 21048, 47219, 56276, 50359, 52169, 467, 23016, 28883], 'labels': [7, 3, -1, 6, -1, -1, 2, -1, -1, 6], 'scores': [0.5755892992019653, 0.39988255500793457, 0.43006372451782227, 0.5822848081588745, 0.3895719647407532, 0.38434794545173645, 0.652188777923584, 0.5186977982521057, 0.42412006855010986, 0.48455169796943665]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.9549980163574219})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.44748756289482117})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.34320035576820374})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.30545955896377563})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2633095681667328})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2849353551864624})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3140590190887451})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3196192979812622})
store['active_learning_steps'][42]['training']['best_epoch']=5
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.9675, 'crossentropy': 0.25532265625}
store['active_learning_steps'][42]['eval_training']={}
store['active_learning_steps'][42]['eval_training']['epochs']=[]
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.8727702498435974})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4462529718875885})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.37373512983322144})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.32478004693984985})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.30097055435180664})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3103868067264557})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.27641206979751587})
store['active_learning_steps'][42]['eval_training']['best_epoch']=7
store['active_learning_steps'][42]['acquisition']={'indices': [15679, 35546, 44767, 36581, 3265, 14524, 37758, 47472, 4687, 14923], 'labels': [2, -1, 2, -1, -1, -1, 0, -1, -1, -1], 'scores': [0.5108442902565002, 0.3640860319137573, 0.19151806831359863, 0.4712851047515869, 0.24836385250091553, 0.44518518447875977, 0.47110629081726074, 0.24217092990875244, 0.44824421405792236, 0.2670564651489258]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.9102954864501953})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.4397062361240387})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3580370545387268})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3283814489841461})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.32028573751449585})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.289004385471344})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.28728607296943665})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.30138760805130005})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3041498363018036})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.28802943229675293})
store['active_learning_steps'][43]['training']['best_epoch']=7
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.9649, 'crossentropy': 0.286697900390625}
store['active_learning_steps'][43]['eval_training']={}
store['active_learning_steps'][43]['eval_training']['epochs']=[]
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.8757023811340332})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.48260295391082764})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.37038981914520264})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3084889352321625})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2972521483898163})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3163822293281555})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.26489242911338806})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.25732359290122986})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2509818375110626})
store['active_learning_steps'][43]['eval_training']['best_epoch']=9
store['active_learning_steps'][43]['acquisition']={'indices': [21144, 30553, 48708, 37075, 57608, 29212, 20119, 21880, 1353, 19127], 'labels': [-1, -1, -1, -1, 3, 7, 6, 2, -1, -1], 'scores': [0.303802490234375, 0.46702122688293457, 0.22531330585479736, 0.3305072784423828, 0.26041001081466675, 0.32027944922447205, 0.45894381403923035, 0.5441281199455261, 0.2774784564971924, 0.35643041133880615]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.9283305406570435})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.5120862126350403})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3345905542373657})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3498835861682892})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.28342196345329285})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2920539379119873})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.26408931612968445})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3118358552455902})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.31347495317459106})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3041810989379883})
store['active_learning_steps'][44]['training']['best_epoch']=7
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.9684, 'crossentropy': 0.2807329345703125}
store['active_learning_steps'][44]['eval_training']={}
store['active_learning_steps'][44]['eval_training']['epochs']=[]
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.8542858958244324})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.49535316228866577})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.360179603099823})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3195496201515198})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.28964531421661377})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2885901629924774})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2902092933654785})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.26501771807670593})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.26957955956459045})
store['active_learning_steps'][44]['eval_training']['best_epoch']=8
store['active_learning_steps'][44]['acquisition']={'indices': [40198, 15505, 6053, 2783, 12635, 6890, 24740, 45786, 19492, 1610], 'labels': [-1, -1, -1, -1, -1, -1, 8, -1, -1, -1], 'scores': [0.3576585650444031, 0.49115073680877686, 0.392101526260376, 0.5117831230163574, 0.4728059768676758, 0.43812787532806396, 0.5118146538734436, 0.4304889440536499, 0.3798222541809082, 0.3248922824859619]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.9492542743682861})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4495815336704254})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.38542795181274414})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.33042484521865845})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.337651789188385})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.34000706672668457})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3623364567756653})
store['active_learning_steps'][45]['training']['best_epoch']=4
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.9649, 'crossentropy': 0.2842409423828125}
store['active_learning_steps'][45]['eval_training']={}
store['active_learning_steps'][45]['eval_training']['epochs']=[]
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.787453293800354})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4945187568664551})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.37301748991012573})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3797714114189148})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3171386420726776})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.311482310295105})
store['active_learning_steps'][45]['eval_training']['best_epoch']=6
store['active_learning_steps'][45]['acquisition']={'indices': [53990, 8575, 10651, 47603, 13998, 51662, 52054, 30444, 15793, 32120], 'labels': [-1, -1, -1, -1, 9, -1, -1, 6, -1, -1], 'scores': [0.3987722396850586, 0.3961905241012573, 0.2886894941329956, 0.3889201879501343, 0.6155949831008911, 0.3277056813240051, 0.2404915690422058, 0.32984352111816406, 0.30484938621520996, 0.47924304008483887]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.938788652420044})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5327652096748352})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.39691174030303955})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.345895916223526})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3344701826572418})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.35292115807533264})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.31298404932022095})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3308591842651367})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.321472704410553})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3618382513523102})
store['active_learning_steps'][46]['training']['best_epoch']=7
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.9668, 'crossentropy': 0.29167470703125}
store['active_learning_steps'][46]['eval_training']={}
store['active_learning_steps'][46]['eval_training']['epochs']=[]
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.8727962970733643})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4906066060066223})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.42432886362075806})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.35734307765960693})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3167524039745331})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.28859400749206543})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3123626708984375})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3065199851989746})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2729882001876831})
store['active_learning_steps'][46]['eval_training']['best_epoch']=9
store['active_learning_steps'][46]['acquisition']={'indices': [56323, 32679, 22320, 31557, 40943, 40944, 32921, 48253, 58129, 2845], 'labels': [9, -1, 8, -1, -1, 1, -1, -1, 9, 8], 'scores': [0.3144056797027588, 0.3810858726501465, 0.48125338554382324, 0.2838701605796814, 0.5005720853805542, 0.42746901512145996, 0.5362175703048706, 0.5591061115264893, 0.4401153326034546, 0.48991963267326355]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.9975906014442444})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4886186718940735})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.37432530522346497})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3334536552429199})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.30169689655303955})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3120887279510498})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3194245398044586})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.33597055077552795})
store['active_learning_steps'][47]['training']['best_epoch']=5
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.9645, 'crossentropy': 0.2856861083984375}
store['active_learning_steps'][47]['eval_training']={}
store['active_learning_steps'][47]['eval_training']['epochs']=[]
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.759046733379364})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4779251217842102})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.374674916267395})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.35552871227264404})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3522491157054901})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2937406897544861})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.30987516045570374})
store['active_learning_steps'][47]['eval_training']['best_epoch']=6
store['active_learning_steps'][47]['acquisition']={'indices': [17296, 3234, 32782, 11017, 32732, 26259, 40873, 50090, 8866, 49966], 'labels': [9, -1, 6, -1, -1, -1, 7, 4, 7, -1], 'scores': [0.4324283003807068, 0.406491756439209, 0.4596734642982483, 0.28911304473876953, 0.1900097131729126, 0.20984315872192383, 0.3200708031654358, 0.4747721552848816, 0.29612934589385986, 0.21245872974395752]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 1.0066102743148804})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.46670183539390564})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4048556089401245})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.31627365946769714})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3292294144630432})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3099098205566406})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3300233781337738})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3045133650302887})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3221963047981262})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3527427911758423})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.33984220027923584})
store['active_learning_steps'][48]['training']['best_epoch']=8
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.9658, 'crossentropy': 0.2827278076171875}
store['active_learning_steps'][48]['eval_training']={}
store['active_learning_steps'][48]['eval_training']['epochs']=[]
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.8544623851776123})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.4967341721057892})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3680083751678467})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2891278862953186})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3027292490005493})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3033828139305115})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.25160008668899536})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2790786623954773})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.24757671356201172})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2514846622943878})
store['active_learning_steps'][48]['eval_training']['best_epoch']=9
store['active_learning_steps'][48]['acquisition']={'indices': [28860, 30382, 13002, 49356, 54814, 50722, 58101, 23849, 1886, 21901], 'labels': [4, -1, 9, -1, 4, -1, 4, -1, -1, -1], 'scores': [0.5727910995483398, 0.5082195997238159, 0.44083327054977417, 0.38650572299957275, 0.5579248070716858, 0.38055455684661865, 0.39909064769744873, 0.2595590353012085, 0.6086775064468384, 0.6117346286773682]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 1.0685651302337646})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5969367623329163})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4311717748641968})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3633692264556885})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.4044925570487976})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3272802531719208})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3625316619873047})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.35068657994270325})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3587394952774048})
store['active_learning_steps'][49]['training']['best_epoch']=6
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.9623, 'crossentropy': 0.294700439453125}
store['active_learning_steps'][49]['eval_training']={}
store['active_learning_steps'][49]['eval_training']['epochs']=[]
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.860263466835022})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.44649603962898254})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3854096233844757})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.34167540073394775})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3285195529460907})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.31415969133377075})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2725410461425781})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.27576518058776855})
store['active_learning_steps'][49]['eval_training']['best_epoch']=7
store['active_learning_steps'][49]['acquisition']={'indices': [4369, 49548, 15012, 41872, 1189, 53215, 13428, 14277, 51722, 7829], 'labels': [-1, 8, -1, -1, -1, -1, 9, 7, 4, -1], 'scores': [0.40107452869415283, 0.20639505982398987, 0.23226463794708252, 0.2736416459083557, 0.3145524263381958, 0.40610015392303467, 0.28116071224212646, 0.39526066184043884, 0.5271487236022949, 0.4989616870880127]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 1.0327427387237549})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5271738767623901})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.39739787578582764})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.35430431365966797})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3346894383430481})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.33033546805381775})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3012966215610504})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.30867815017700195})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.33095550537109375})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.33744460344314575})
store['active_learning_steps'][50]['training']['best_epoch']=7
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.9685, 'crossentropy': 0.26290966796875}
store['active_learning_steps'][50]['eval_training']={}
store['active_learning_steps'][50]['eval_training']['epochs']=[]
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.8512976169586182})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.50434410572052})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.39304155111312866})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3670387864112854})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2893068790435791})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2800256907939911})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.26384198665618896})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.30262452363967896})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.28141453862190247})
store['active_learning_steps'][50]['eval_training']['best_epoch']=7
store['active_learning_steps'][50]['acquisition']={'indices': [25508, 49626, 22977, 13488, 36107, 45784, 50644, 21601, 59481, 39015], 'labels': [5, -1, -1, -1, -1, 9, 3, 1, -1, -1], 'scores': [0.529212236404419, 0.296303391456604, 0.4299851655960083, 0.39354825019836426, 0.4643765687942505, 0.43194788694381714, 0.4519362449645996, 0.5170760154724121, 0.4138141870498657, 0.479026734828949]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.8999677896499634})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5103983283042908})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3792586922645569})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3167109489440918})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.32777005434036255})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.30937618017196655})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.28767895698547363})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3328074812889099})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3140329122543335})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.30042362213134766})
store['active_learning_steps'][51]['training']['best_epoch']=7
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.9676, 'crossentropy': 0.2537659912109375}
store['active_learning_steps'][51]['eval_training']={}
store['active_learning_steps'][51]['eval_training']['epochs']=[]
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.7551091313362122})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.43355584144592285})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.35754862427711487})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3100649118423462})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.31720995903015137})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2938811779022217})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.2689155638217926})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.26819783449172974})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2562621831893921})
store['active_learning_steps'][51]['eval_training']['best_epoch']=9
store['active_learning_steps'][51]['acquisition']={'indices': [26952, 59276, 48665, 46974, 49877, 41630, 33062, 39079, 55145, 120], 'labels': [-1, -1, -1, 2, -1, -1, -1, -1, -1, -1], 'scores': [0.3943312168121338, 0.29358839988708496, 0.5013003349304199, 0.3165879547595978, 0.341499924659729, 0.48688340187072754, 0.31364989280700684, 0.5216449499130249, 0.3070485591888428, 0.4620124101638794]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 1.0025315284729004})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5316644906997681})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.388537734746933})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3519691824913025})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.34491807222366333})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3172389268875122})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3189975619316101})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.33865171670913696})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.31837576627731323})
store['active_learning_steps'][52]['training']['best_epoch']=6
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.9679, 'crossentropy': 0.2661861083984375}
store['active_learning_steps'][52]['eval_training']={}
store['active_learning_steps'][52]['eval_training']['epochs']=[]
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.8838405609130859})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.5124911665916443})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4106624126434326})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3446163535118103})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.33059078454971313})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3280673027038574})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.2986016869544983})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.29237014055252075})
store['active_learning_steps'][52]['eval_training']['best_epoch']=8
store['active_learning_steps'][52]['acquisition']={'indices': [5224, 17871, 49064, 3361, 53761, 23927, 42504, 52195, 15534, 37596], 'labels': [-1, -1, 8, -1, -1, 5, 8, -1, -1, 7], 'scores': [0.4486358165740967, 0.47705554962158203, 0.5789169669151306, 0.3502727746963501, 0.31971275806427, 0.6143532395362854, 0.4339883327484131, 0.24348998069763184, 0.3561614751815796, 0.4726867377758026]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.9662438631057739})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5236706733703613})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3918449878692627})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.35347235202789307})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.31356602907180786})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3322872221469879})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3095289170742035})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3370402753353119})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.36579376459121704})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.346388578414917})
store['active_learning_steps'][53]['training']['best_epoch']=7
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.9694, 'crossentropy': 0.26001923828125}
store['active_learning_steps'][53]['eval_training']={}
store['active_learning_steps'][53]['eval_training']['epochs']=[]
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.8130853176116943})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4564589262008667})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.37481728196144104})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.348978728055954})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.28854602575302124})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3177645802497864})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.2793537974357605})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2779853343963623})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.27023011445999146})
store['active_learning_steps'][53]['eval_training']['best_epoch']=9
store['active_learning_steps'][53]['acquisition']={'indices': [4322, 45888, 51474, 11708, 58832, 59289, 53976, 55310, 37307, 3694], 'labels': [2, 9, -1, 3, 3, 1, 9, 1, 2, -1], 'scores': [0.30328598618507385, 0.46152400970458984, 0.1424311399459839, 0.3837694525718689, 0.5204331278800964, 0.5748859643936157, 0.3838992416858673, 0.4864348769187927, 0.40304484963417053, 0.5574299693107605]}
store['active_learning_steps'].append({})
store['active_learning_steps'][54]['training']={}
store['active_learning_steps'][54]['training']['epochs']=[]
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.9358625411987305})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.5043498873710632})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3817655146121979})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3142664134502411})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3391454815864563})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3099614381790161})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3320908546447754})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3103489875793457})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.29978147149086})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3125973045825958})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.33871549367904663})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.33004868030548096})
store['active_learning_steps'][54]['training']['best_epoch']=9
store['active_learning_steps'][54]['evaluation_metrics']={'accuracy': 0.9682, 'crossentropy': 0.2553443603515625}
store['active_learning_steps'][54]['eval_training']={}
store['active_learning_steps'][54]['eval_training']['epochs']=[]
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.8957223892211914})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.46836981177330017})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.38628146052360535})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3332037627696991})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3147934079170227})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.30393242835998535})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.30404454469680786})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.2612744867801666})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2879927158355713})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.25988444685935974})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.27477678656578064})
store['active_learning_steps'][54]['eval_training']['best_epoch']=10
store['active_learning_steps'][54]['acquisition']={'indices': [40216, 34486, 1275, 32981, 53460, 37399, 39661, 45716, 529, 29723], 'labels': [7, 0, -1, -1, -1, -1, -1, -1, -1, 5], 'scores': [0.4832850694656372, 0.43638908863067627, 0.41640961170196533, 0.32709836959838867, 0.3726729154586792, 0.43022841215133667, 0.4097755551338196, 0.34096431732177734, 0.342349648475647, 0.5135256350040436]}
store['active_learning_steps'].append({})
store['active_learning_steps'][55]['training']={}
store['active_learning_steps'][55]['training']['epochs']=[]
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 1.0195062160491943})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4725661277770996})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3406279683113098})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3434075117111206})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3194793462753296})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.32968658208847046})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3217816948890686})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3150821626186371})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.35279008746147156})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3317822813987732})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.35140281915664673})
store['active_learning_steps'][55]['training']['best_epoch']=8
store['active_learning_steps'][55]['evaluation_metrics']={'accuracy': 0.9707, 'crossentropy': 0.2552734619140625}
store['active_learning_steps'][55]['eval_training']={}
store['active_learning_steps'][55]['eval_training']['epochs']=[]
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.817740261554718})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.45860886573791504})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.37044283747673035})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.34506791830062866})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2866016626358032})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.29380446672439575})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.26781782507896423})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2326267808675766})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.262632817029953})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.27669015526771545})
store['active_learning_steps'][55]['eval_training']['best_epoch']=8
store['active_learning_steps'][55]['acquisition']={'indices': [45016, 18862, 16690, 59838, 56449, 18277, 39018, 43176, 28225, 32715], 'labels': [-1, -1, -1, -1, -1, -1, -1, 2, -1, -1], 'scores': [0.47552013397216797, 0.3327730894088745, 0.4795372486114502, 0.39058566093444824, 0.36913013458251953, 0.39895039796829224, 0.35926276445388794, 0.59248948097229, 0.3884192705154419, 0.37145572900772095]}
store['active_learning_steps'].append({})
store['active_learning_steps'][56]['training']={}
store['active_learning_steps'][56]['training']['epochs']=[]
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.9534140229225159})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4936769902706146})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4117380976676941})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.34856075048446655})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3182752728462219})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3021714687347412})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3333253860473633})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.353213369846344})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.322892427444458})
store['active_learning_steps'][56]['training']['best_epoch']=6
store['active_learning_steps'][56]['evaluation_metrics']={'accuracy': 0.9703, 'crossentropy': 0.2525417236328125}
store['active_learning_steps'][56]['eval_training']={}
store['active_learning_steps'][56]['eval_training']['epochs']=[]
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.8498340845108032})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.42412781715393066})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.42263686656951904})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.34463295340538025})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.31903478503227234})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.29586851596832275})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2775610089302063})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.27749043703079224})
store['active_learning_steps'][56]['eval_training']['best_epoch']=8
store['active_learning_steps'][56]['acquisition']={'indices': [24976, 1488, 30480, 9433, 22991, 17183, 23962, 43288, 30769, 32372], 'labels': [-1, -1, -1, 7, -1, -1, 3, -1, -1, 5], 'scores': [0.3808128833770752, 0.3895726203918457, 0.3463212251663208, 0.553625613451004, 0.4284713864326477, 0.5503475666046143, 0.41161346435546875, 0.474589467048645, 0.45071327686309814, 0.5245531797409058]}
store['active_learning_steps'].append({})
store['active_learning_steps'][57]['training']={}
store['active_learning_steps'][57]['training']['epochs']=[]
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 1.027023434638977})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5590872764587402})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.3976307511329651})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3567691445350647})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3103386461734772})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.32822394371032715})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3343544900417328})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.36974358558654785})
store['active_learning_steps'][57]['training']['best_epoch']=5
store['active_learning_steps'][57]['evaluation_metrics']={'accuracy': 0.9659, 'crossentropy': 0.2719158203125}
store['active_learning_steps'][57]['eval_training']={}
store['active_learning_steps'][57]['eval_training']['epochs']=[]
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.8273577094078064})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.5340520143508911})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.39328789710998535})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3535865545272827})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3408946692943573})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.30490022897720337})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.27866852283477783})
store['active_learning_steps'][57]['eval_training']['best_epoch']=7
store['active_learning_steps'][57]['acquisition']={'indices': [59726, 42002, 57718, 54253, 6497, 59390, 51556, 14331, 45510, 248], 'labels': [5, -1, 7, -1, -1, 2, -1, -1, -1, -1], 'scores': [0.6524254679679871, 0.3348652124404907, 0.515783965587616, 0.4834439754486084, 0.3889061212539673, 0.5109919309616089, 0.31680476665496826, 0.49080705642700195, 0.585832953453064, 0.4755122661590576]}
store['active_learning_steps'].append({})
store['active_learning_steps'][58]['training']={}
store['active_learning_steps'][58]['training']['epochs']=[]
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.9578946828842163})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4792223572731018})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3693414330482483})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.32948511838912964})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.37152621150016785})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.31922078132629395})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.32403767108917236})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3267394006252289})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.319183349609375})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.336323082447052})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3325692415237427})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.35759517550468445})
store['active_learning_steps'][58]['training']['best_epoch']=9
store['active_learning_steps'][58]['evaluation_metrics']={'accuracy': 0.9703, 'crossentropy': 0.2555625}
store['active_learning_steps'][58]['eval_training']={}
store['active_learning_steps'][58]['eval_training']['epochs']=[]
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.8021687865257263})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.46920180320739746})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3651018738746643})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.32214638590812683})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.28604620695114136})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.292680561542511})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2541080415248871})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2715698778629303})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2762143015861511})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.27338147163391113})
store['active_learning_steps'][58]['eval_training']['best_epoch']=7
store['active_learning_steps'][58]['acquisition']={'indices': [21981, 18201, 59439, 17781, 35530, 52033, 54917, 45602, 11216, 51818], 'labels': [-1, -1, -1, -1, -1, -1, 7, 5, -1, -1], 'scores': [0.5579315423965454, 0.5046195983886719, 0.42385220527648926, 0.5130653381347656, 0.27399301528930664, 0.5875881910324097, 0.46473342180252075, 0.5050705373287201, 0.42108404636383057, 0.36655282974243164]}
store['active_learning_steps'].append({})
store['active_learning_steps'][59]['training']={}
store['active_learning_steps'][59]['training']['epochs']=[]
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 1.0307531356811523})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.5127838850021362})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.39902210235595703})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3365364074707031})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3177851736545563})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.31134581565856934})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.30912864208221436})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.32380247116088867})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3694431185722351})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.33382660150527954})
store['active_learning_steps'][59]['training']['best_epoch']=7
store['active_learning_steps'][59]['evaluation_metrics']={'accuracy': 0.9692, 'crossentropy': 0.2539364990234375}
store['active_learning_steps'][59]['eval_training']={}
store['active_learning_steps'][59]['eval_training']['epochs']=[]
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.8476520776748657})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5456889867782593})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.38973283767700195})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3597695231437683})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.35796141624450684})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.27996826171875})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.29675984382629395})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.31192827224731445})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2724836468696594})
store['active_learning_steps'][59]['eval_training']['best_epoch']=9
store['active_learning_steps'][59]['acquisition']={'indices': [59884, 38701, 49070, 45084, 30418, 26405, 22170, 34407, 53854, 52670], 'labels': [-1, -1, 2, -1, 8, 9, -1, 3, 8, -1], 'scores': [0.31866276264190674, 0.41872578859329224, 0.48481351137161255, 0.5688999891281128, 0.5251835584640503, 0.5627949237823486, 0.3383779525756836, 0.36871859431266785, 0.43168288469314575, 0.34783613681793213]}
store['active_learning_steps'].append({})
store['active_learning_steps'][60]['training']={}
store['active_learning_steps'][60]['training']['epochs']=[]
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 1.063279151916504})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.498577356338501})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.41082972288131714})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3540705442428589})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.30468523502349854})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3485952317714691})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.32973748445510864})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3301410675048828})
store['active_learning_steps'][60]['training']['best_epoch']=5
store['active_learning_steps'][60]['evaluation_metrics']={'accuracy': 0.9685, 'crossentropy': 0.267330224609375}
store['active_learning_steps'][60]['eval_training']={}
store['active_learning_steps'][60]['eval_training']['epochs']=[]
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.9066972136497498})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5143755078315735})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.4288323223590851})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.37228816747665405})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3189117908477783})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3301110863685608})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.33951568603515625})
store['active_learning_steps'][60]['eval_training']['best_epoch']=5
store['active_learning_steps'][60]['acquisition']={'indices': [15967, 58765, 591, 35546, 30085, 49171, 12890, 42265, 14074, 27023], 'labels': [-1, -1, -1, -1, 9, -1, -1, 7, 5, -1], 'scores': [0.32103967666625977, 0.3720129728317261, 0.2819375991821289, 0.4160940647125244, 0.4880130887031555, 0.3169652223587036, 0.41322624683380127, 0.39770787954330444, 0.3705897927284241, 0.30943799018859863]}
store['active_learning_steps'].append({})
store['active_learning_steps'][61]['training']={}
store['active_learning_steps'][61]['training']['epochs']=[]
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.9793601632118225})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5219427347183228})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3857998549938202})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.34817445278167725})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3141556978225708})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3554471433162689})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3302016854286194})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.31071192026138306})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.32001644372940063})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.34113436937332153})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3384256958961487})
store['active_learning_steps'][61]['training']['best_epoch']=8
store['active_learning_steps'][61]['evaluation_metrics']={'accuracy': 0.9687, 'crossentropy': 0.2604848876953125}
store['active_learning_steps'][61]['eval_training']={}
store['active_learning_steps'][61]['eval_training']['epochs']=[]
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.9194942712783813})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.48534590005874634})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.38079333305358887})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3319433331489563})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2958643436431885})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3079010844230652})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.27260491251945496})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3085020184516907})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2583094835281372})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.25916799902915955})
store['active_learning_steps'][61]['eval_training']['best_epoch']=9
store['active_learning_steps'][61]['acquisition']={'indices': [1155, 25310, 58427, 19524, 55368, 31474, 57342, 14514, 56457, 24404], 'labels': [-1, 1, -1, 2, 8, 8, 2, -1, -1, -1], 'scores': [0.3997917175292969, 0.40190786123275757, 0.2956188917160034, 0.40751540660858154, 0.47405385971069336, 0.6128588914871216, 0.4355549216270447, 0.4585556983947754, 0.3950510025024414, 0.5844081044197083]}
store['active_learning_steps'].append({})
store['active_learning_steps'][62]['training']={}
store['active_learning_steps'][62]['training']['epochs']=[]
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.0674331188201904})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5380433201789856})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3977199196815491})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.32783079147338867})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.32099270820617676})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.31338047981262207})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.30811047554016113})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.30660486221313477})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.32166025042533875})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.33135420083999634})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.32438796758651733})
store['active_learning_steps'][62]['training']['best_epoch']=8
store['active_learning_steps'][62]['evaluation_metrics']={'accuracy': 0.9723, 'crossentropy': 0.2607204345703125}
store['active_learning_steps'][62]['eval_training']={}
store['active_learning_steps'][62]['eval_training']['epochs']=[]
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.914547324180603})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.48114562034606934})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.35536250472068787})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.32915419340133667})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2813066244125366})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.29465529322624207})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2860795855522156})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2797083258628845})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.2696859538555145})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2567061483860016})
store['active_learning_steps'][62]['eval_training']['best_epoch']=10
store['active_learning_steps'][62]['acquisition']={'indices': [6291, 19495, 27427, 45739, 25673, 34775, 38806, 1037, 1116, 57507], 'labels': [3, 3, -1, 9, -1, -1, -1, -1, 9, 0], 'scores': [0.5591744184494019, 0.5855719447135925, 0.3243652582168579, 0.45563262701034546, 0.37821412086486816, 0.3838251829147339, 0.40691208839416504, 0.326815128326416, 0.3706350028514862, 0.6149455308914185]}
store['active_learning_steps'].append({})
store['active_learning_steps'][63]['training']={}
store['active_learning_steps'][63]['training']['epochs']=[]
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 1.0663816928863525})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5050328373908997})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3971543312072754})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.33361560106277466})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3324943780899048})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.28545844554901123})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.29968398809432983})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.30553197860717773})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.31315523386001587})
store['active_learning_steps'][63]['training']['best_epoch']=6
store['active_learning_steps'][63]['evaluation_metrics']={'accuracy': 0.97, 'crossentropy': 0.2546108642578125}
store['active_learning_steps'][63]['eval_training']={}
store['active_learning_steps'][63]['eval_training']['epochs']=[]
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.9883676767349243})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.49112677574157715})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.39422228932380676})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3474329113960266})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.31347304582595825})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.27248233556747437})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2808680534362793})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2680566906929016})
store['active_learning_steps'][63]['eval_training']['best_epoch']=8
store['active_learning_steps'][63]['acquisition']={'indices': [52196, 19931, 11319, 19789, 23546, 27446, 6213, 32499, 40589, 39267], 'labels': [-1, -1, -1, -1, 5, -1, -1, 4, 2, 3], 'scores': [0.4061744213104248, 0.3828155994415283, 0.3447688817977905, 0.5903041958808899, 0.37302500009536743, 0.33419716358184814, 0.33434343338012695, 0.33177071809768677, 0.4475123882293701, 0.3074166774749756]}
store['active_learning_steps'].append({})
store['active_learning_steps'][64]['training']={}
store['active_learning_steps'][64]['training']['epochs']=[]
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 1.0547189712524414})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5323418378829956})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.387006938457489})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.335684210062027})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.31268686056137085})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2922620177268982})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2948530614376068})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.34244999289512634})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.29412537813186646})
store['active_learning_steps'][64]['training']['best_epoch']=6
store['active_learning_steps'][64]['evaluation_metrics']={'accuracy': 0.9714, 'crossentropy': 0.251216650390625}
store['active_learning_steps'][64]['eval_training']={}
store['active_learning_steps'][64]['eval_training']['epochs']=[]
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.874382495880127})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.5266276597976685})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.389651358127594})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.34421393275260925})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.31993764638900757})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.321685254573822})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2975274324417114})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.31632405519485474})
store['active_learning_steps'][64]['eval_training']['best_epoch']=7
store['active_learning_steps'][64]['acquisition']={'indices': [15475, 33658, 4457, 45559, 55585, 31988, 43684, 50505, 21264, 41557], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.44793087244033813, 0.563785195350647, 0.6169700622558594, 0.5166759490966797, 0.5775570869445801, 0.464174747467041, 0.47553378343582153, 0.5189575552940369, 0.36946558952331543, 0.725954532623291]}
store['active_learning_steps'].append({})
store['active_learning_steps'][65]['training']={}
store['active_learning_steps'][65]['training']['epochs']=[]
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 1.0235919952392578})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5521913766860962})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.40416768193244934})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3170015513896942})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3263174891471863})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.30479809641838074})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.33611196279525757})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.37888234853744507})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3592855632305145})
store['active_learning_steps'][65]['training']['best_epoch']=6
store['active_learning_steps'][65]['evaluation_metrics']={'accuracy': 0.9708, 'crossentropy': 0.2571160400390625}
store['active_learning_steps'][65]['eval_training']={}
store['active_learning_steps'][65]['eval_training']['epochs']=[]
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.8720240592956543})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4870568513870239})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3912423849105835})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.363639771938324})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3481149673461914})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.30561864376068115})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2809332311153412})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2609270215034485})
store['active_learning_steps'][65]['eval_training']['best_epoch']=8
store['active_learning_steps'][65]['acquisition']={'indices': [40766, 49138, 24531, 40378, 30917, 2831, 51318, 475, 26072, 5790], 'labels': [4, -1, 3, -1, -1, -1, -1, -1, 1, 2], 'scores': [0.4621581435203552, 0.34861648082733154, 0.5607678890228271, 0.4739161729812622, 0.3671523928642273, 0.2168886661529541, 0.4872487783432007, 0.3757164478302002, 0.3953934907913208, 0.37560194730758667]}
store['active_learning_steps'].append({})
store['active_learning_steps'][66]['training']={}
store['active_learning_steps'][66]['training']['epochs']=[]
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 1.1301608085632324})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5541268587112427})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3854941725730896})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3179727792739868})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.294869601726532})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.28551745414733887})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.29962635040283203})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2720180153846741})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2760891914367676})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.31907281279563904})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.32900696992874146})
store['active_learning_steps'][66]['training']['best_epoch']=8
store['active_learning_steps'][66]['evaluation_metrics']={'accuracy': 0.9717, 'crossentropy': 0.2490705322265625}
store['active_learning_steps'][66]['eval_training']={}
store['active_learning_steps'][66]['eval_training']['epochs']=[]
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.8942861557006836})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.5380380153656006})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.4220065474510193})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3728415369987488})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.31014484167099})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2947676181793213})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2988506555557251})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.27310866117477417})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2731133699417114})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2533435523509979})
store['active_learning_steps'][66]['eval_training']['best_epoch']=10
store['active_learning_steps'][66]['acquisition']={'indices': [52244, 23036, 13259, 13021, 53054, 35149, 2597, 58188, 1238, 54378], 'labels': [-1, -1, 1, 5, -1, -1, -1, -1, -1, -1], 'scores': [0.3670504093170166, 0.2505764961242676, 0.4114462733268738, 0.5134491324424744, 0.6802568435668945, 0.4014507532119751, 0.40411317348480225, 0.2590246796607971, 0.42469286918640137, 0.4764225482940674]}
store['active_learning_steps'].append({})
store['active_learning_steps'][67]['training']={}
store['active_learning_steps'][67]['training']['epochs']=[]
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 1.072751522064209})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5864995718002319})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4327039122581482})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.327484667301178})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.32782965898513794})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2987034022808075})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3111417889595032})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.31117552518844604})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2975970506668091})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.34570014476776123})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.3139271140098572})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.31024688482284546})
store['active_learning_steps'][67]['training']['best_epoch']=9
store['active_learning_steps'][67]['evaluation_metrics']={'accuracy': 0.9745, 'crossentropy': 0.2399212158203125}
store['active_learning_steps'][67]['eval_training']={}
store['active_learning_steps'][67]['eval_training']['epochs']=[]
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.8455092906951904})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.45626598596572876})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3523295819759369})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3019971251487732})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3173149824142456})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.27570265531539917})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.26155948638916016})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.27095383405685425})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.23718881607055664})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.25864455103874207})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.27360570430755615})
store['active_learning_steps'][67]['eval_training']['best_epoch']=9
store['active_learning_steps'][67]['acquisition']={'indices': [17092, 9186, 26404, 29260, 57706, 19576, 6425, 53700, 47523, 55778], 'labels': [-1, -1, -1, -1, -1, 9, -1, 9, -1, -1], 'scores': [0.3184767961502075, 0.4129441976547241, 0.45033693313598633, 0.4625648260116577, 0.47876107692718506, 0.5241876840591431, 0.4467158317565918, 0.41206562519073486, 0.29965198040008545, 0.6832568645477295]}
store['active_learning_steps'].append({})
store['active_learning_steps'][68]['training']={}
store['active_learning_steps'][68]['training']['epochs']=[]
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 1.0034173727035522})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5520409941673279})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.37750178575515747})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3693762421607971})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.33819863200187683})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3247276544570923})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.327200710773468})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3238220810890198})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3535762429237366})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.34005826711654663})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.34084299206733704})
store['active_learning_steps'][68]['training']['best_epoch']=8
store['active_learning_steps'][68]['evaluation_metrics']={'accuracy': 0.9689, 'crossentropy': 0.2617073974609375}
store['active_learning_steps'][68]['eval_training']={}
store['active_learning_steps'][68]['eval_training']['epochs']=[]
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.9339135885238647})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.538418710231781})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.397920161485672})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.37071967124938965})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.32724565267562866})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3021809458732605})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.32345056533813477})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.29088205099105835})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.29226720333099365})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.29744845628738403})
store['active_learning_steps'][68]['eval_training']['best_epoch']=8
store['active_learning_steps'][68]['acquisition']={'indices': [51582, 23736, 32242, 26169, 34920, 10479, 57728, 4432, 27968, 28110], 'labels': [-1, -1, -1, -1, -1, -1, 9, -1, 9, -1], 'scores': [0.38024187088012695, 0.3926050662994385, 0.40852677822113037, 0.32602977752685547, 0.43989551067352295, 0.611686110496521, 0.5338842868804932, 0.6466359496116638, 0.4272199273109436, 0.44732922315597534]}
store['active_learning_steps'].append({})
store['active_learning_steps'][69]['training']={}
store['active_learning_steps'][69]['training']['epochs']=[]
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 1.1658127307891846})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.524589478969574})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.40275317430496216})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.34741514921188354})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.32016417384147644})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3143705725669861})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3381233811378479})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.33839380741119385})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.36373043060302734})
store['active_learning_steps'][69]['training']['best_epoch']=6
store['active_learning_steps'][69]['evaluation_metrics']={'accuracy': 0.9697, 'crossentropy': 0.2665949462890625}
store['active_learning_steps'][69]['eval_training']={}
store['active_learning_steps'][69]['eval_training']['epochs']=[]
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.8831521272659302})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5052263140678406})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.41895443201065063})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.37690305709838867})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3693374991416931})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.314092755317688})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.30354297161102295})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.29248520731925964})
store['active_learning_steps'][69]['eval_training']['best_epoch']=8
store['active_learning_steps'][69]['acquisition']={'indices': [20150, 19837, 13003, 28932, 22930, 40014, 46013, 20746, 33691, 59771], 'labels': [3, -1, -1, 2, -1, -1, 6, 1, -1, -1], 'scores': [0.500370979309082, 0.558867335319519, 0.37484121322631836, 0.3111785650253296, 0.30954694747924805, 0.3464066982269287, 0.18867862224578857, 0.5308939814567566, 0.21760046482086182, 0.3090725541114807]}
store['active_learning_steps'].append({})
store['active_learning_steps'][70]['training']={}
store['active_learning_steps'][70]['training']['epochs']=[]
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 1.0887032747268677})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.5376884937286377})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.41523057222366333})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3617461919784546})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3414650559425354})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.35614013671875})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.34810900688171387})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.33210280537605286})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.32728880643844604})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3243166506290436})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3117014169692993})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.34190431237220764})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.34716206789016724})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.34964483976364136})
store['active_learning_steps'][70]['training']['best_epoch']=11
store['active_learning_steps'][70]['evaluation_metrics']={'accuracy': 0.9718, 'crossentropy': 0.2648667236328125}
store['active_learning_steps'][70]['eval_training']={}
store['active_learning_steps'][70]['eval_training']['epochs']=[]
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.9301134347915649})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5135185718536377})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.4471883773803711})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.32889634370803833})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3224526643753052})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3019729554653168})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3128203749656677})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.29674750566482544})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2693709135055542})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2752308249473572})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2584512233734131})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2725553810596466})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2664981484413147})
store['active_learning_steps'][70]['eval_training']['best_epoch']=11
store['active_learning_steps'][70]['acquisition']={'indices': [49026, 1886, 34713, 37339, 47597, 22700, 21990, 51992, 37389, 54521], 'labels': [6, -1, 3, 4, 8, -1, 1, -1, -1, -1], 'scores': [0.41991475224494934, 0.30399346351623535, 0.3938905596733093, 0.6240772306919098, 0.5295889973640442, 0.4121389389038086, 0.4397962689399719, 0.4787580966949463, 0.29803240299224854, 0.24587726593017578]}
store['active_learning_steps'].append({})
store['active_learning_steps'][71]['training']={}
store['active_learning_steps'][71]['training']['epochs']=[]
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 1.0650177001953125})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.5021143555641174})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.41891059279441833})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.35195279121398926})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.29376116394996643})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3242211937904358})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3074735403060913})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2540077865123749})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2915712594985962})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2990732789039612})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.30122047662734985})
store['active_learning_steps'][71]['training']['best_epoch']=8
store['active_learning_steps'][71]['evaluation_metrics']={'accuracy': 0.9731, 'crossentropy': 0.23680458984375}
store['active_learning_steps'][71]['eval_training']={}
store['active_learning_steps'][71]['eval_training']['epochs']=[]
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.8847022652626038})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.47917041182518005})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3689683973789215})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.31743961572647095})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.298517644405365})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.28543469309806824})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2824849486351013})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.26821786165237427})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.27593374252319336})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2629377245903015})
store['active_learning_steps'][71]['eval_training']['best_epoch']=10
store['active_learning_steps'][71]['acquisition']={'indices': [7271, 3367, 4564, 18292, 8200, 2765, 37280, 19251, 55910, 39672], 'labels': [0, 0, -1, -1, 3, 0, -1, -1, -1, 7], 'scores': [0.6035046577453613, 0.5509026050567627, 0.5085741281509399, 0.5741201639175415, 0.43592995405197144, 0.5630549192428589, 0.4255683422088623, 0.5638965368270874, 0.5628086924552917, 0.37411755323410034]}
store['active_learning_steps'].append({})
store['active_learning_steps'][72]['training']={}
store['active_learning_steps'][72]['training']['epochs']=[]
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 1.0252028703689575})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.5663323402404785})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3637409210205078})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.330945760011673})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2987266778945923})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3188358545303345})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.3127204477787018})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2947571277618408})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.29934969544410706})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3065672814846039})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3087347447872162})
store['active_learning_steps'][72]['training']['best_epoch']=8
store['active_learning_steps'][72]['evaluation_metrics']={'accuracy': 0.9734, 'crossentropy': 0.250605810546875}
store['active_learning_steps'][72]['eval_training']={}
store['active_learning_steps'][72]['eval_training']['epochs']=[]
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.9289803504943848})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4791068732738495})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.4052892029285431})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3356221914291382})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.31575992703437805})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.30581802129745483})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2990993559360504})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.28641772270202637})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.27092915773391724})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2632681429386139})
store['active_learning_steps'][72]['eval_training']['best_epoch']=10
store['active_learning_steps'][72]['acquisition']={'indices': [42403, 52624, 13243, 50736, 12694, 20784, 14062, 2034, 90, 9184], 'labels': [-1, -1, -1, -1, -1, 5, 8, 4, -1, -1], 'scores': [0.43902087211608887, 0.4639040231704712, 0.4824979305267334, 0.537076473236084, 0.3032466173171997, 0.4968448281288147, 0.5152348875999451, 0.40824222564697266, 0.32422810792922974, 0.5031945705413818]}
store['active_learning_steps'].append({})
store['active_learning_steps'][73]['training']={}
store['active_learning_steps'][73]['training']['epochs']=[]
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.9232271909713745})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4829632043838501})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4255533814430237})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.33529132604599})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.26652729511260986})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2847754657268524})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.27880868315696716})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2753159999847412})
store['active_learning_steps'][73]['training']['best_epoch']=5
store['active_learning_steps'][73]['evaluation_metrics']={'accuracy': 0.9691, 'crossentropy': 0.263716796875}
store['active_learning_steps'][73]['eval_training']={}
store['active_learning_steps'][73]['eval_training']['epochs']=[]
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.9139125943183899})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.46260422468185425})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.4176948070526123})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.34114086627960205})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.37793850898742676})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.31129586696624756})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3125111758708954})
store['active_learning_steps'][73]['eval_training']['best_epoch']=6
store['active_learning_steps'][73]['acquisition']={'indices': [59081, 13488, 16156, 5950, 44505, 44071, 24303, 20230, 31406, 2481], 'labels': [-1, -1, -1, -1, -1, -1, -1, 4, -1, -1], 'scores': [0.47332286834716797, 0.4650907516479492, 0.40444159507751465, 0.42304348945617676, 0.44717586040496826, 0.30873239040374756, 0.4714040756225586, 0.45109373331069946, 0.47545814514160156, 0.34134340286254883]}
store['active_learning_steps'].append({})
store['active_learning_steps'][74]['training']={}
store['active_learning_steps'][74]['training']['epochs']=[]
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.2430384159088135})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6475059390068054})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.418351948261261})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3511231541633606})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3238930404186249})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.33123838901519775})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3222348690032959})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3078003525733948})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3080379366874695})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.30696016550064087})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.34372878074645996})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3136710524559021})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.32442671060562134})
store['active_learning_steps'][74]['training']['best_epoch']=10
store['active_learning_steps'][74]['evaluation_metrics']={'accuracy': 0.9718, 'crossentropy': 0.252683935546875}
store['active_learning_steps'][74]['eval_training']={}
store['active_learning_steps'][74]['eval_training']['epochs']=[]
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.9364305734634399})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.49552440643310547})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.4240010380744934})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3256036043167114})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.33921897411346436})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.26796388626098633})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3051750063896179})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.27933424711227417})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.26161372661590576})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2482200711965561})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2567620277404785})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2659597098827362})
store['active_learning_steps'][74]['eval_training']['best_epoch']=10
store['active_learning_steps'][74]['acquisition']={'indices': [27998, 24630, 24239, 22175, 53991, 32108, 9279, 49985, 17161, 3848], 'labels': [-1, 5, -1, 8, -1, 4, -1, 3, -1, -1], 'scores': [0.5264042615890503, 0.499983012676239, 0.28703898191452026, 0.3985297679901123, 0.2975326180458069, 0.5690627098083496, 0.37730783224105835, 0.3904097080230713, 0.37479060888290405, 0.2892226576805115]}
store['active_learning_steps'].append({})
store['active_learning_steps'][75]['training']={}
store['active_learning_steps'][75]['training']['epochs']=[]
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 1.0486738681793213})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5556702017784119})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.4013442099094391})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3559367060661316})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3549698293209076})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3354766368865967})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.33259689807891846})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.29031527042388916})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2877647280693054})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.33629101514816284})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.30486422777175903})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.31401169300079346})
store['active_learning_steps'][75]['training']['best_epoch']=9
store['active_learning_steps'][75]['evaluation_metrics']={'accuracy': 0.9737, 'crossentropy': 0.248274755859375}
store['active_learning_steps'][75]['eval_training']={}
store['active_learning_steps'][75]['eval_training']['epochs']=[]
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.9671651124954224})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5379521250724792})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.38072988390922546})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.32181257009506226})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3042411208152771})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2738547921180725})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2655017375946045})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.24461713433265686})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.26295167207717896})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2561867833137512})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.26676562428474426})
store['active_learning_steps'][75]['eval_training']['best_epoch']=8
store['active_learning_steps'][75]['acquisition']={'indices': [45520, 17182, 36606, 32906, 59857, 47669, 44581, 746, 56066, 34920], 'labels': [8, 4, 9, 7, -1, 3, -1, -1, 7, 9], 'scores': [0.42420047521591187, 0.2976064085960388, 0.33478623628616333, 0.4724853038787842, 0.24486035108566284, 0.32745862007141113, 0.5016387701034546, 0.269004225730896, 0.46166419982910156, 0.4926011562347412]}
store['active_learning_steps'].append({})
store['active_learning_steps'][76]['training']={}
store['active_learning_steps'][76]['training']['epochs']=[]
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 1.1212294101715088})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4929986596107483})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.39397376775741577})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3440120220184326})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.30094343423843384})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3020244240760803})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2854013442993164})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2730939984321594})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.31029778718948364})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3204520046710968})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2764281630516052})
store['active_learning_steps'][76]['training']['best_epoch']=8
store['active_learning_steps'][76]['evaluation_metrics']={'accuracy': 0.9705, 'crossentropy': 0.23871728515625}
store['active_learning_steps'][76]['eval_training']={}
store['active_learning_steps'][76]['eval_training']['epochs']=[]
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.9356142282485962})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5106128454208374})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3944983184337616})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.33789747953414917})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3248937726020813})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.28820300102233887})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.28843235969543457})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.26838216185569763})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.26244795322418213})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.27130740880966187})
store['active_learning_steps'][76]['eval_training']['best_epoch']=9
store['active_learning_steps'][76]['acquisition']={'indices': [5633, 47960, 3932, 2627, 59188, 15978, 32880, 16701, 3798, 49822], 'labels': [-1, -1, -1, -1, -1, -1, 0, -1, 7, -1], 'scores': [0.37194883823394775, 0.4095282554626465, 0.4816581606864929, 0.37203747034072876, 0.49406659603118896, 0.37046194076538086, 0.5944455862045288, 0.4759872555732727, 0.5164655447006226, 0.33633023500442505]}
store['active_learning_steps'].append({})
store['active_learning_steps'][77]['training']={}
store['active_learning_steps'][77]['training']['epochs']=[]
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 1.1095561981201172})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.553491473197937})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.4330562949180603})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.35392799973487854})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.33855777978897095})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.27505022287368774})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.29669713973999023})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2777809202671051})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3037528693675995})
store['active_learning_steps'][77]['training']['best_epoch']=6
store['active_learning_steps'][77]['evaluation_metrics']={'accuracy': 0.9709, 'crossentropy': 0.2609129638671875}
store['active_learning_steps'][77]['eval_training']={}
store['active_learning_steps'][77]['eval_training']['epochs']=[]
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.9201622009277344})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5339380502700806})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.4452829957008362})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3671005368232727})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.36586612462997437})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.30398231744766235})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3146457076072693})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3057457506656647})
store['active_learning_steps'][77]['eval_training']['best_epoch']=6
store['active_learning_steps'][77]['acquisition']={'indices': [52590, 22526, 45440, 1075, 45042, 26557, 31017, 39776, 37962, 20177], 'labels': [-1, -1, 9, 7, -1, 8, -1, -1, 8, -1], 'scores': [0.4839779734611511, 0.21541988849639893, 0.3445364832878113, 0.6435749530792236, 0.2771369218826294, 0.3375999331474304, 0.266831636428833, 0.27993571758270264, 0.3707120418548584, 0.39588236808776855]}
store['active_learning_steps'].append({})
store['active_learning_steps'][78]['training']={}
store['active_learning_steps'][78]['training']['epochs']=[]
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 1.1037589311599731})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5991508364677429})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.39459913969039917})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.32447537779808044})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.307137668132782})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2957858443260193})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2592906951904297})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.28764796257019043})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2838394045829773})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.28834694623947144})
store['active_learning_steps'][78]['training']['best_epoch']=7
store['active_learning_steps'][78]['evaluation_metrics']={'accuracy': 0.9731, 'crossentropy': 0.232832177734375}
store['active_learning_steps'][78]['eval_training']={}
store['active_learning_steps'][78]['eval_training']['epochs']=[]
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.8289042711257935})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.46429288387298584})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3773394525051117})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.34265729784965515})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.32197391986846924})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2974473834037781})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.28670257329940796})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2738812565803528})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.32064321637153625})
store['active_learning_steps'][78]['eval_training']['best_epoch']=8
store['active_learning_steps'][78]['acquisition']={'indices': [45908, 8118, 51650, 36940, 29479, 9901, 23343, 40382, 670, 41267], 'labels': [-1, 8, 7, -1, -1, -1, -1, 3, 3, 3], 'scores': [0.5120300054550171, 0.28975576162338257, 0.3887273371219635, 0.267447829246521, 0.24557602405548096, 0.33862149715423584, 0.2960951328277588, 0.20792318880558014, 0.3559742569923401, 0.2726471424102783]}
store['active_learning_steps'].append({})
store['active_learning_steps'][79]['training']={}
store['active_learning_steps'][79]['training']['epochs']=[]
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 1.0282618999481201})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.5070182085037231})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.39018714427948})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.34806227684020996})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2909477949142456})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2961440086364746})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3030451536178589})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.25634557008743286})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.29932376742362976})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.26794689893722534})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2791006565093994})
store['active_learning_steps'][79]['training']['best_epoch']=8
store['active_learning_steps'][79]['evaluation_metrics']={'accuracy': 0.9733, 'crossentropy': 0.2286049072265625}
