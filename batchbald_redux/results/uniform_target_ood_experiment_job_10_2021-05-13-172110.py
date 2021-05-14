store = {}
store['timestamp']=1620922870
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/uniform_target_ood_experiment.py', '--id=10']
store['commit']='7a88a46c213fc419b8e48358058ec72fe5b0f546'
store['github_url']='7a88a46c213fc419b8e48358058ec72fe5b0f546'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/uniform_target_ood_experiment.py'
store['job_id']=10
store['worker_id']=10
store['num_workers']=20
store['config']={'seed': 1249, 'acquisition_size': 10, 'max_training_set': 450, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'evaluation_set_size': 100, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'min_samples_per_epoch': 5056, 'mnist_repetitions': 1, 'ood_fmnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.TemperedEvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples) | one_hot_targets{'num_classes': 10}) + ('OoD Dataset (60000 samples)' | uniform_targets{'num_classes': 10})", 'test': "'FastMNIST (test, 10000 samples)'"}
store['initial_training_set_indices']=[53434, 8533, 14640, 39579, 30392, 58125, 37915, 3091, 57520, 43803, 44119, 52296, 58226, 40334, 46037, 22015, 22304, 43812, 12640, 53689]
store['evaluation_set_indices']=[29974, 55573, 35472, 44048, 48031, 5616, 10110, 47420, 56990, 34198, 3792, 5715, 15969, 32775, 19757, 34588, 28991, 47417, 26501, 12108, 5573, 48032, 40646, 43252, 2404, 36797, 29079, 40018, 37047, 41512, 45567, 801, 10664, 52801, 42890, 32972, 45974, 20801, 23496, 5803, 10508, 46870, 49549, 306, 38725, 13074, 19689, 27135, 16068, 18137, 2728, 43321, 29950, 380, 27254, 50466, 31965, 24052, 44454, 20076, 21423, 58741, 27145, 38430, 37354, 49986, 4321, 12610, 34482, 35794, 396, 50036, 46861, 57811, 53831, 49304, 51555, 29614, 767, 23451, 49512, 26479, 50997, 1774, 44803, 55187, 30013, 33736, 49169, 46464, 31444, 52440, 33486, 2206, 15675, 54426, 9574, 54012, 28833, 44428]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.1137166023254395})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 2.2941315174102783})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 2.829442024230957})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 2.3553199768066406})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6785, 'crossentropy': 1.9317615234375}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.1459364891052246})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.18696928024292})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.1400997638702393})
store['active_learning_steps'][0]['eval_training']['best_epoch']=3
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 47902], ['id', 14614], ['ood', 55658], ['id', 54077], ['id', 8046], ['id', 23637], ['ood', 25898], ['ood', 31008], ['id', 11792], ['id', 42919]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.7124983072280884, 1.0230488777160645, 0.45723605155944824, 0.7582705020904541, 0.8209189772605896, 0.496219277381897, 0.36402297019958496, 0.6552962064743042, 0.7298620343208313, 0.5814248323440552]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.3722386360168457})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.7115790843963623})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.8056750297546387})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.8566553592681885})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.7161, 'crossentropy': 1.275581640625}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.1264441013336182})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.0602288246154785})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.0372462272644043})
store['active_learning_steps'][1]['eval_training']['best_epoch']=3
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 59368], ['id', 19365], ['id', 13804], ['id', 608], ['id', 37324], ['ood', 5831], ['id', 25720], ['id', 43045], ['id', 36957], ['id', 44808]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.356189489364624, 0.39652419090270996, 0.5009551048278809, 0.38101351261138916, 0.3725518584251404, 0.2323765754699707, 0.48044008016586304, 0.4099491834640503, 0.4052923917770386, 0.41985464096069336]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.2959423065185547})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.5260025262832642})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.894802451133728})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.7718991041183472})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.7364, 'crossentropy': 1.267039453125}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.0388221740722656})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 0.9787405133247375})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 0.9966083765029907})
store['active_learning_steps'][2]['eval_training']['best_epoch']=2
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 19677], ['id', 21042], ['id', 27130], ['id', 8097], ['id', 53878], ['id', 55896], ['id', 30782], ['id', 31177], ['id', 57013], ['id', 52631]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.48921358585357666, 0.4496093988418579, 0.559175968170166, 0.4491238594055176, 0.4342118501663208, 0.4043271541595459, 0.561913251876831, 0.49871546030044556, 0.2845684289932251, 0.4354979395866394]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.755859375, 'crossentropy': 1.1220279932022095})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 1.2021726369857788})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7626953125, 'crossentropy': 1.35808527469635})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7783203125, 'crossentropy': 1.3645825386047363})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.78, 'crossentropy': 1.01421728515625}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.7470703125, 'crossentropy': 0.9878705739974976})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.763671875, 'crossentropy': 0.8749914169311523})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.765625, 'crossentropy': 0.9194303750991821})
store['active_learning_steps'][3]['eval_training']['best_epoch']=2
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 27479], ['id', 54493], ['id', 12950], ['id', 4958], ['id', 16997], ['id', 51261], ['id', 25429], ['id', 3636], ['ood', 6296], ['id', 41993]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.2736837863922119, 0.43813520669937134, 0.5183309316635132, 0.41972601413726807, 0.3306403160095215, 0.2963595390319824, 0.5359372496604919, 0.3274444341659546, 0.13657963275909424, 0.26752758026123047]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.765625, 'crossentropy': 1.0882995128631592})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.765625, 'crossentropy': 1.3739607334136963})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7822265625, 'crossentropy': 1.3026317358016968})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.783203125, 'crossentropy': 1.4535467624664307})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.7958, 'crossentropy': 0.99890078125}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.759765625, 'crossentropy': 0.9536503553390503})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.7724609375, 'crossentropy': 0.8805221319198608})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.755859375, 'crossentropy': 0.8883392810821533})
store['active_learning_steps'][4]['eval_training']['best_epoch']=2
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 53019], ['id', 36655], ['id', 39080], ['id', 32249], ['id', 39593], ['id', 47365], ['id', 15402], ['id', 48832], ['id', 38593], ['id', 36790]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5443627238273621, 0.32314157485961914, 0.477632999420166, 0.395763099193573, 0.49478161334991455, 0.5393148064613342, 0.5850158929824829, 0.338765025138855, 0.40141934156417847, 0.41119736433029175]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 0.9994629621505737})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.9172590970993042})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 0.9974748492240906})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 1.1337380409240723})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.0872914791107178})
store['active_learning_steps'][5]['training']['best_epoch']=2
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.8381, 'crossentropy': 0.82464521484375}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.8063753843307495})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 0.7856601476669312})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.6997740864753723})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.6645033359527588})
store['active_learning_steps'][5]['eval_training']['best_epoch']=4
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 25718], ['id', 24170], ['id', 32734], ['id', 17342], ['id', 25321], ['id', 21998], ['id', 44350], ['id', 19638], ['id', 28276], ['id', 45161]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.30421388149261475, 0.4299006462097168, 0.4572112560272217, 0.23039966821670532, 0.5620807409286499, 0.4478100538253784, 0.5867332220077515, 0.5510382056236267, 0.3992964029312134, 0.4032667279243469]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 0.9646642208099365})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 0.9916702508926392})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 0.9376499652862549})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 1.0917314291000366})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 1.312901496887207})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 1.3141628503799438})
store['active_learning_steps'][6]['training']['best_epoch']=3
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.851, 'crossentropy': 0.82130478515625}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 0.8450651168823242})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.7150897979736328})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.6944195032119751})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.6556484699249268})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.6427300572395325})
store['active_learning_steps'][6]['eval_training']['best_epoch']=5
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 1097], ['id', 22684], ['id', 3095], ['id', 47506], ['id', 28192], ['id', 59080], ['id', 33484], ['id', 48066], ['id', 57236], ['id', 1272]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.31161344051361084, 0.5170774459838867, 0.46780216693878174, 0.5564126372337341, 0.5461077690124512, 0.5014340281486511, 0.40249118208885193, 0.3225683569908142, 0.5228539705276489, 0.6290942430496216]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 0.9630057215690613})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.8387478590011597})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.8663432598114014})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.9965966939926147})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.9478263854980469})
store['active_learning_steps'][7]['training']['best_epoch']=2
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.8508, 'crossentropy': 0.761173193359375}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 0.8218618035316467})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.6702283620834351})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.6297820806503296})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.6466206312179565})
store['active_learning_steps'][7]['eval_training']['best_epoch']=3
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 50202], ['id', 53344], ['id', 21451], ['id', 24569], ['id', 24939], ['id', 55090], ['id', 3356], ['id', 3496], ['id', 21151], ['id', 8614]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.4121279716491699, 0.4618849754333496, 0.5061283707618713, 0.3480202853679657, 0.34768104553222656, 0.2915976047515869, 0.31843990087509155, 0.3577837347984314, 0.38173866271972656, 0.44496023654937744]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 0.8981291651725769})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.8147802948951721})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.0000420808792114})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.8750336170196533})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.926683783531189})
store['active_learning_steps'][8]['training']['best_epoch']=2
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.8636, 'crossentropy': 0.719328076171875}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.8184589147567749})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.6619553565979004})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.593246340751648})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.5638046264648438})
store['active_learning_steps'][8]['eval_training']['best_epoch']=4
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 21007], ['id', 51610], ['id', 27011], ['id', 12658], ['id', 38688], ['id', 15127], ['id', 45826], ['id', 1457], ['id', 47484], ['id', 11822]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.284748911857605, 0.5306078791618347, 0.25760042667388916, 0.401212215423584, 0.42411547899246216, 0.4029540419578552, 0.44221270084381104, 0.3487223982810974, 0.327592670917511, 0.4755532741546631]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 0.915703296661377})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 0.8012193441390991})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.768807590007782})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.7972574234008789})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.8653503656387329})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.9613827466964722})
store['active_learning_steps'][9]['training']['best_epoch']=3
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.8728, 'crossentropy': 0.715018505859375}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.7959750294685364})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.6626870632171631})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.5835350751876831})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.5753197073936462})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.5793498754501343})
store['active_learning_steps'][9]['eval_training']['best_epoch']=4
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 8619], ['ood', 29018], ['id', 40382], ['id', 36421], ['id', 1772], ['id', 28844], ['id', 29416], ['id', 50802], ['id', 24906], ['id', 54056]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.44317734241485596, 0.3629704713821411, 0.40471798181533813, 0.36707037687301636, 0.43435001373291016, 0.37315183877944946, 0.24085187911987305, 0.40958529710769653, 0.4533088207244873, 0.45325928926467896]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.8486853837966919})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7061475515365601})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.661016047000885})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.722885012626648})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.7595483064651489})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7357828617095947})
store['active_learning_steps'][10]['training']['best_epoch']=3
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.8936, 'crossentropy': 0.626633203125}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.7810742855072021})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.6475663185119629})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.5543580651283264})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.5240524411201477})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.5182775259017944})
store['active_learning_steps'][10]['eval_training']['best_epoch']=5
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 5626], ['id', 56995], ['id', 30089], ['id', 41525], ['id', 535], ['id', 20206], ['id', 8423], ['id', 20195], ['id', 56076], ['id', 11684]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.4631114602088928, 0.5043603181838989, 0.5398368835449219, 0.523654580116272, 0.5392206907272339, 0.310788094997406, 0.437602698802948, 0.5442373752593994, 0.4827873110771179, 0.44826364517211914]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7405363917350769})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5263754725456238})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5296272039413452})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5345003604888916})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5370311737060547})
store['active_learning_steps'][11]['training']['best_epoch']=2
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.9194, 'crossentropy': 0.4775041015625}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7125207781791687})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5638431906700134})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5449488759040833})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.4684109687805176})
store['active_learning_steps'][11]['eval_training']['best_epoch']=4
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 48503], ['id', 18150], ['id', 14878], ['ood', 45410], ['id', 49515], ['ood', 4073], ['id', 8438], ['id', 42096], ['id', 49537], ['id', 24473]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.3898097276687622, 0.3525715470314026, 0.4281797409057617, 0.27759766578674316, 0.4846459627151489, 0.2972133159637451, 0.3326287269592285, 0.45701897144317627, 0.4163781404495239, 0.44323599338531494]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.8084256649017334})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5517498254776001})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5408903360366821})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5197040438652039})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5422507524490356})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5357166528701782})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6096940040588379})
store['active_learning_steps'][12]['training']['best_epoch']=4
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.9271, 'crossentropy': 0.4608396484375}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7320065498352051})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5044199228286743})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.4465254545211792})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.41902995109558105})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.4242991805076599})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.40956538915634155})
store['active_learning_steps'][12]['eval_training']['best_epoch']=6
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 43497], ['id', 29751], ['id', 16652], ['id', 27120], ['id', 46187], ['id', 43906], ['id', 12767], ['id', 59716], ['id', 50353], ['id', 29621]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.2515014410018921, 0.32465171813964844, 0.29456543922424316, 0.3509884476661682, 0.5505409836769104, 0.44074296951293945, 0.4882688522338867, 0.24762487411499023, 0.4213486909866333, 0.592595100402832]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.7462831735610962})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5056735277175903})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5012235045433044})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.46016478538513184})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.48695114254951477})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5175743103027344})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5171932578086853})
store['active_learning_steps'][13]['training']['best_epoch']=4
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.9329, 'crossentropy': 0.4068585693359375}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.7058011293411255})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.4836740791797638})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.4546273946762085})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.42105281352996826})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4081045985221863})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4130815863609314})
store['active_learning_steps'][13]['eval_training']['best_epoch']=5
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 7886], ['id', 22532], ['id', 40456], ['id', 30351], ['id', 21890], ['id', 48512], ['id', 43648], ['id', 58303], ['id', 23622], ['id', 33294]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.42598849534988403, 0.359544038772583, 0.3791350722312927, 0.4114829897880554, 0.25543543696403503, 0.5536242723464966, 0.5728830695152283, 0.4312548041343689, 0.34848326444625854, 0.39190149307250977]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7877775430679321})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.46028605103492737})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4156877398490906})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.41834214329719543})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.41714978218078613})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.45895442366600037})
store['active_learning_steps'][14]['training']['best_epoch']=3
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.9394, 'crossentropy': 0.3812206298828125}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6845334768295288})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.513401448726654})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.4602402448654175})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4061758518218994})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.39059120416641235})
store['active_learning_steps'][14]['eval_training']['best_epoch']=5
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 17486], ['ood', 19272], ['id', 32835], ['ood', 29936], ['id', 7207], ['id', 3712], ['id', 16044], ['id', 42504], ['id', 3094], ['id', 57276]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.41537028551101685, 0.2738898992538452, 0.28652775287628174, 0.29917407035827637, 0.33344340324401855, 0.31017643213272095, 0.38565540313720703, 0.5276574492454529, 0.4079463481903076, 0.37201863527297974]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.8597939014434814})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5403414368629456})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5398590564727783})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.48772069811820984})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4810096025466919})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4653151035308838})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5411838293075562})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5572071671485901})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5574809312820435})
store['active_learning_steps'][15]['training']['best_epoch']=6
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.9362, 'crossentropy': 0.40914716796875}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.7443259954452515})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.48992079496383667})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.44133567810058594})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4046415686607361})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.39089435338974})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.40674489736557007})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.3968944549560547})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.372386634349823})
store['active_learning_steps'][15]['eval_training']['best_epoch']=8
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 4955], ['id', 35725], ['id', 6152], ['id', 13156], ['id', 33995], ['id', 47720], ['id', 31738], ['id', 15873], ['id', 52878], ['id', 12347]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.44700902700424194, 0.34666162729263306, 0.3803097903728485, 0.49441206455230713, 0.44140446186065674, 0.3885120153427124, 0.6702302098274231, 0.4723195433616638, 0.41217583417892456, 0.5100289583206177]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.892592191696167})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5408540964126587})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.4484041929244995})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5144807696342468})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4683397114276886})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5279864072799683})
store['active_learning_steps'][16]['training']['best_epoch']=3
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.9385, 'crossentropy': 0.4193919921875}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.7766589522361755})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5192108750343323})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5005019307136536})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.48214972019195557})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.44283556938171387})
store['active_learning_steps'][16]['eval_training']['best_epoch']=5
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 14796], ['id', 46086], ['id', 56191], ['id', 12938], ['id', 25238], ['id', 39835], ['id', 22278], ['id', 15206], ['id', 52895], ['id', 45888]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.3708011507987976, 0.4676828384399414, 0.485393762588501, 0.37375086545944214, 0.2781064510345459, 0.35116320848464966, 0.3758915066719055, 0.28090161085128784, 0.4064827561378479, 0.3956531286239624]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.8123799562454224})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5296072959899902})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4483422040939331})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4278203845024109})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.48589450120925903})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5049859285354614})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.44610828161239624})
store['active_learning_steps'][17]['training']['best_epoch']=4
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.9407, 'crossentropy': 0.391502294921875}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.7188091278076172})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.47470277547836304})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.44584640860557556})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.38115036487579346})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.41318970918655396})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.39959707856178284})
store['active_learning_steps'][17]['eval_training']['best_epoch']=4
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 12211], ['id', 3762], ['id', 13002], ['id', 54756], ['id', 14715], ['id', 58384], ['id', 19868], ['id', 51136], ['id', 35686], ['id', 1352]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.24765276908874512, 0.47382187843322754, 0.3687450885772705, 0.5416164398193359, 0.43111175298690796, 0.43650543689727783, 0.5979369282722473, 0.2719370126724243, 0.3481972813606262, 0.4796183109283447]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.8423062562942505})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5196713209152222})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.45180976390838623})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.45541995763778687})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.47246474027633667})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4873501658439636})
store['active_learning_steps'][18]['training']['best_epoch']=3
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.9456, 'crossentropy': 0.3966320068359375}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.8186897039413452})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5618785619735718})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.45906615257263184})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4153140187263489})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.42916762828826904})
store['active_learning_steps'][18]['eval_training']['best_epoch']=4
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 47499], ['id', 29880], ['id', 609], ['id', 24542], ['id', 2892], ['id', 964], ['id', 30135], ['id', 32702], ['id', 37435], ['id', 21297]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.4064751863479614, 0.507687509059906, 0.1766808032989502, 0.4606929421424866, 0.35884612798690796, 0.43874168395996094, 0.32313257455825806, 0.377768874168396, 0.4827413558959961, 0.2903643846511841]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.9213212728500366})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.49541008472442627})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.46049678325653076})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.46737533807754517})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.46743685007095337})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.4718461036682129})
store['active_learning_steps'][19]['training']['best_epoch']=3
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.9405, 'crossentropy': 0.3928998291015625}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.7007555365562439})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5110677480697632})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.4569610357284546})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.4478772282600403})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.4439448118209839})
store['active_learning_steps'][19]['eval_training']['best_epoch']=5
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 13983], ['id', 42995], ['id', 42711], ['id', 32093], ['id', 50297], ['id', 28373], ['id', 55395], ['id', 2412], ['id', 31562], ['id', 29361]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5414565801620483, 0.33962440490722656, 0.5520175099372864, 0.29736030101776123, 0.45969855785369873, 0.4757148027420044, 0.4421621561050415, 0.46753543615341187, 0.44724732637405396, 0.49718940258026123]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.9398626089096069})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5602364540100098})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4352811574935913})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.39821457862854004})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.44277721643447876})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.40779760479927063})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.41927623748779297})
store['active_learning_steps'][20]['training']['best_epoch']=4
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.9554, 'crossentropy': 0.3375921630859375}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7313917875289917})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.4595687985420227})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4103657603263855})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.342693567276001})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.37161731719970703})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.3804681897163391})
store['active_learning_steps'][20]['eval_training']['best_epoch']=4
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 59287], ['id', 7029], ['id', 24883], ['id', 13829], ['id', 5260], ['id', 38050], ['id', 48449], ['id', 35034], ['id', 38022], ['id', 760]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.4054560661315918, 0.45171254873275757, 0.42718106508255005, 0.46532130241394043, 0.4060993492603302, 0.570409893989563, 0.18740898370742798, 0.4016803205013275, 0.3623011112213135, 0.33051204681396484]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.8899024128913879})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5341649055480957})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4064633250236511})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.39394986629486084})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.42588937282562256})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.40858712792396545})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4009447693824768})
store['active_learning_steps'][21]['training']['best_epoch']=4
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.9495, 'crossentropy': 0.3624423583984375}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7444580793380737})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.48574721813201904})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.3915182650089264})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.367040753364563})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.35500913858413696})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.32574498653411865})
store['active_learning_steps'][21]['eval_training']['best_epoch']=6
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 9402], ['id', 44590], ['id', 5172], ['id', 48775], ['id', 35786], ['id', 22824], ['ood', 28361], ['id', 28881], ['id', 41713], ['id', 58213]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.3858060836791992, 0.31669721007347107, 0.4083048701286316, 0.43583792448043823, 0.40595078468322754, 0.5180213451385498, 0.2663320302963257, 0.38157665729522705, 0.3896888196468353, 0.4631536602973938]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7971560955047607})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4748179018497467})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.40518224239349365})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3842577338218689})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.371349036693573})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.35918956995010376})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.38441967964172363})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3633134961128235})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3776776194572449})
store['active_learning_steps'][22]['training']['best_epoch']=6
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.9603, 'crossentropy': 0.2862234130859375}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.8058729767799377})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.43656888604164124})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.3607926368713379})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.3469209372997284})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.30514270067214966})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3039873242378235})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.28929010033607483})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.2910659611225128})
store['active_learning_steps'][22]['eval_training']['best_epoch']=7
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 14152], ['ood', 24389], ['id', 45850], ['id', 39778], ['id', 57690], ['id', 29180], ['id', 24533], ['id', 20029], ['id', 24110], ['id', 5679]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.45428401231765747, 0.18805670738220215, 0.41439634561538696, 0.6363381147384644, 0.47925886511802673, 0.4873536229133606, 0.44214946031570435, 0.47007861733436584, 0.35511571168899536, 0.41558539867401123]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.9266507029533386})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5432832837104797})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.40571120381355286})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4248817563056946})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4149690270423889})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4449913799762726})
store['active_learning_steps'][23]['training']['best_epoch']=3
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.9489, 'crossentropy': 0.359252392578125}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7314298152923584})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.48626428842544556})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.47663766145706177})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.48026013374328613})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.43105417490005493})
store['active_learning_steps'][23]['eval_training']['best_epoch']=5
store['active_learning_steps'][23]['acquisition']={'indices': [['ood', 26952], ['id', 36984], ['id', 50091], ['id', 3358], ['id', 48115], ['id', 20486], ['id', 37059], ['id', 41134], ['id', 27292], ['ood', 21004]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.25531792640686035, 0.3088453412055969, 0.3192804455757141, 0.3649822473526001, 0.43536269664764404, 0.535130500793457, 0.4155789613723755, 0.34918642044067383, 0.3556879758834839, 0.23650407791137695]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.9741860628128052})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5049247741699219})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.39211946725845337})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.41790342330932617})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3797992765903473})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3707565665245056})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.36900466680526733})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3741200566291809})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3804260492324829})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.37961098551750183})
store['active_learning_steps'][24]['training']['best_epoch']=7
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.9594, 'crossentropy': 0.310851416015625}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.7715246081352234})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.43111610412597656})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4082024097442627})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.36023885011672974})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3251466751098633})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3505728244781494})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.33705800771713257})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.31390008330345154})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.298262357711792})
store['active_learning_steps'][24]['eval_training']['best_epoch']=9
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 20190], ['id', 16562], ['id', 50088], ['id', 30844], ['id', 916], ['id', 47076], ['id', 21663], ['id', 13021], ['id', 49056], ['id', 32880]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5192997455596924, 0.4521868824958801, 0.5500090718269348, 0.6222164630889893, 0.5380368232727051, 0.6310479044914246, 0.3546099066734314, 0.31471264362335205, 0.46345001459121704, 0.4391288757324219]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.931684672832489})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4619845747947693})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3559015393257141})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3402630686759949})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.37231096625328064})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.36813199520111084})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3634124994277954})
store['active_learning_steps'][25]['training']['best_epoch']=4
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.9559, 'crossentropy': 0.3123052978515625}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7622910737991333})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.47854915261268616})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.39418673515319824})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.35273903608322144})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3475359082221985})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.34417301416397095})
store['active_learning_steps'][25]['eval_training']['best_epoch']=6
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 20050], ['id', 40728], ['id', 50660], ['id', 15743], ['id', 17657], ['id', 7033], ['id', 31650], ['id', 45047], ['id', 19380], ['id', 51974]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.35383903980255127, 0.4496421813964844, 0.3820587992668152, 0.34705114364624023, 0.37044376134872437, 0.5286314487457275, 0.3338964581489563, 0.2384563684463501, 0.27517539262771606, 0.37571728229522705]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 1.0788936614990234})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.51233971118927})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.40667545795440674})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3503544330596924})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3482176661491394})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3199329376220703})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.33897989988327026})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3250998556613922})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.35009312629699707})
store['active_learning_steps'][26]['training']['best_epoch']=6
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.9628, 'crossentropy': 0.2704031005859375}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.7763230800628662})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5138640403747559})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3814498782157898})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.37422236800193787})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.39391201734542847})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.33750712871551514})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.33798331022262573})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3227629065513611})
store['active_learning_steps'][26]['eval_training']['best_epoch']=8
